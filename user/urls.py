from django.urls import path
from .views import RegisterViewAPI, LoginAPIView, VerifyEmail,  RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterViewAPI.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email '),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete '),

]