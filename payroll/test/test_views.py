from user.tests.test_setup import TestSetup
from user.models import User


def get_super_user():
    admin_user = User.objects.create_user(username='admin', email="example@gmail.com", password='adminpass')
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()

    return admin_user


class TestViews(TestSetup):

    def test_create_salary_payment(self):

        admin_user = get_super_user()
        self.client.force_authenticate(user=admin_user)

        data = {
            "salary_employee_payment": 10000
        }
        response = self.client.post(self.salary_payment, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_salary_payments(self):

        admin_user = get_super_user()
        self.client.force_authenticate(user=admin_user)

        response = self.client.get(self.salary_payment)
        self.assertEqual(response.status_code, 200)

    def test_create_commission_payment(self):

        admin_user = get_super_user()
        self.client.force_authenticate(user=admin_user)

        data = {
            "commission_employee_payemnt": 25000,
            "commission_rate": 0.05
        }
        response = self.client.post(self.commission_payment, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_commission_payments(self):

        admin_user = get_super_user()
        self.client.force_authenticate(user=admin_user)

        response = self.client.get(self.commission_payment)
        self.assertEqual(response.status_code, 200)
