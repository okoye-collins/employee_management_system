from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .utils import Util
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, SetNewPasswordSerializer, RequestPasswordRestEmailSerialer

import jwt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class RegisterViewAPI(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://'+current_site+relative_link+"?token="+str(token)
        email_body = f'Hi {user.username} Use link to verify you email \n {absurl}'

        data = {
            'domain': absurl,
            'to_email': user.email,
            'email_subject': "verify your email",
            'email_body': email_body
        }
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyEmail(GenericAPIView):

    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_404_NOT_FOUND)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class RequestPasswordResetEmail(GenericAPIView):

    serializer_class = RequestPasswordRestEmailSerialer

    def post(self, request):

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(str(user.id).encode('utf-8'))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request).domain
            relative_link = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relative_link
            email_body = f'Hello, \n Use this link to reset your password  \n {absurl}'

            data = {
                'domain': absurl,
                'to_email': user.email,
                'email_subject': "Reset your Password",
                'email_body': email_body
            }
            Util.send_email(data)

        return Response({'success': "We have sent you a link to reset your password"}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(GenericAPIView):

    def get_serializer(self, *args, **kwargs):
        return None

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Credentials valid', 'uibd64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(GenericAPIView):

    serializer_class = SetNewPasswordSerializer

    def patch(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': True, 'message': 'password reset success'}, status=status.HTTP_200_OK)


# class NotFoundView(GenericAPIView):
#     def get(self, request):
#         return Response({'error': 'Route not found'}, status=404)
    
class ReturnUserAPIView(GenericAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = LoginSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)