from django.urls import path
from .views import SalaryPaymentAPIView, SalaryPaymentDetailAPIView, CommissionPaymentDetailAPIView, CommissionPaymentAPIView, UserPayRollAPIView, UserPayRollDetailAPIView
# , PayrollDetailAPIView

urlpatterns = [
    path('salary_payment/', SalaryPaymentAPIView.as_view(), name="Salary-Payment"),
    path('salary_payment_detail/<int:pk>/', SalaryPaymentDetailAPIView.as_view(), name="salary-payment-detail"),
    path('commission_payment/', CommissionPaymentAPIView.as_view(), name="commission-payment"),
    path('commission_payment_detail/<int:pk>/', CommissionPaymentDetailAPIView.as_view(), name="commission_payment_detail"),
    path('user_payroll/', UserPayRollAPIView.as_view(), name="user-payroll"),
    path('user_payroll_detail/<int:pk>/', UserPayRollDetailAPIView.as_view(), name="user_payroll_detail"),
    
]