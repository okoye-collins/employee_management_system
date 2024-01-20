from django.db import models
from user.models import User

# Create your models here.


class SalaryPayment(models.Model):
    salary_employee_payment = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' Salary Employee Payment: {self.salary_employee_payment}'


class CommissionPayment(models.Model):
    commission_employee_payemnt = models.DecimalField(max_digits=10, decimal_places=2)
    # i.e 0.05 = 5% commission rate
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text= 'example 0.05 = 5%')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' Commission Employee Payment: {self.commission_employee_payemnt}'


class Payroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customers_brought = models.PositiveIntegerField(default=0)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} Payroll'
