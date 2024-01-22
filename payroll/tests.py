from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import SalaryPayment, CommissionPayment, Payroll


class SalaryPaymentAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('Salary-Payment')

    def test_create_salary_payment(self):
        data = {
            "salary_employee_payment": 10000
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_salary_payments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommissionPaymentAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('commission-payment')

    def test_create_commission_payment(self):
        data = {
            "commission_employee_payemnt": 25000,
            "commission_rate": 0.05
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_commission_payments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserPayrollAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-payroll')

    def test_create_user_payroll(self):
        data = {{
            "user": 1,
            "customers_brought": 3
}
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_user_payrolls(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
