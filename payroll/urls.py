from django.urls import path
from .views import SalaryPaymentAPIView, SalaryPaymentDetailAPIView, CommissionPaymentDetailAPIView, CommissionPaymentAPIView
# , PayrollDetailAPIView

urlpatterns = [
    path('salary_payment/', SalaryPaymentAPIView.as_view(), name="Salary-Payment"),
    path('salary_payment_detail/<int:pk>/', SalaryPaymentDetailAPIView.as_view(), name="salary-payment-detail"),
    path('commission_payment/', CommissionPaymentAPIView.as_view(), name="commission_payment"),
    path('commission_payment_detail/<int:pk>/', CommissionPaymentDetailAPIView.as_view(), name="commission_payment_detail"),
    
]