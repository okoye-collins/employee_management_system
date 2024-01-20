from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .serializers import PayRollSerializer, SalaryPaymentSerializer, CommissionPaymentSerializer
from .models import Payroll, SalaryPayment, CommissionPayment

# Create your views here.


class SalaryPaymentAPIView(GenericAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = SalaryPaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.validate(raise_exception=True)
        serializer.save()

        return Response({'message': 'Salary Payment has been created Successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):

        salary_payment = SalaryPayment.objects.all()
        serializer = self.serializer_class(salary_payment, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SalaryPaymentDetailAPIView(GenericAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = SalaryPaymentSerializer

    def put(self, request, pk):
        try:
            salary_payment = SalaryPayment.objects.get(id=pk)
        except Exception as e:
            return Response({'message': 'Salary Payment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(salary_payment, data=request.data)
        serializer.validate(raise_exception=True)
        serializer.save()
        return Response({'message': 'Salary payment has been Updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            salary_payment = SalaryPayment.objects.get(id=pk)
        except Exception as e:
            return Response({'message': 'Salary Payment not found'}, status=status.HTTP_404_NOT_FOUND)

        salary_payment.delete()
        return Response({'message': 'Salary Payment has been deleted successfully'}, status=status.HTTP_200_OK)


class CommissionPaymentAPIView(GenericAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = CommissionPaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.validate(raise_exception=True)
        serializer.save()

        return Response({'message': 'Commission Payment has been created Successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):

        commission_payment = CommissionPayment.objects.all()
        serializer = self.serializer_class(commission_payment, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CommissionPaymentDetailAPIView(GenericAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = CommissionPaymentSerializer

    def put(self, request, pk):
        try:
            commission_payment = CommissionPayment.objects.get(id=pk)
        except Exception as e:
            return Response({'Message': 'Commission Payement not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(commission_payment, data=request.data)
        serializer.validate(raise_exception=True)
        serializer.save()
        return Response({'message': 'Commission payment has been Updated successfully'}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            commission_payment = CommissionPayment.objects.get(id=pk)
        except Exception as e:
            return Response({'message': 'Commission Payment not found'}, status=status.HTTP_404_NOT_FOUND)

        commission_payment.delete()
        return Response({'message': 'Commission Payment has been deleted successfully'}, status=status.HTTP_200_OK)
