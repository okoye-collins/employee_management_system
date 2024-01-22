from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

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