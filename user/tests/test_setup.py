from rest_framework.test import APITestCase
from django.urls import reverse
from user.models import User


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.salary_payment = reverse('Salary-Payment')
        self.commission_payment = reverse('commission-payment')

        self.user_data_1 = {
            'email': 'example@gmail.com',
            'username': 'example',
            'employee_type': 'Salary', 
            'password': 'example@gmail.com',
        }

        self.user_data_2 = {
            'email': 'example@gmail.com',
            'username': 'example',
            'employee_type': 'Commission', 
            'password': 'example@gmail.com',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()