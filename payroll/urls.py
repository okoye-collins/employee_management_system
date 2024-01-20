from django.urls import path
from .views import SalaryPaymentAPIView, SalaryPaymentDetailAPIView
# , PayrollDetailAPIView

urlpatterns = [
    path('salary_payment/', SalaryPaymentAPIView.as_view(), name="Salary-Payment"),
    path('salary_payment_/<int:pk>/', SalaryPaymentDetailAPIView.as_view(), name="salary-payment-detail"),
]