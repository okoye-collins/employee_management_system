from .test_setup import TestSetup

from user.models import User

class TestViews(TestSetup):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_salary_employee_user_can_register(self):
        res = self.client.post(
            self.register_url, self.user_data_1, format="json")
        self.assertEqual(res.status_code, 201)

    def test_commission_employee_user_can_register(self):
        res = self.client.post(self.register_url, self.user_data_2, format="json")

        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_unverified_email(self):
        self.client.post(self.register_url, self.user_data_2, format="json")
        res = self.client.post(self.login_url, self.user_data_2, format="json")

        self.assertEqual(res.status_code, 401)

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data_2, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data_2, format="json")
        
        self.assertEqual(res.status_code, 200)



