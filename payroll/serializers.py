from rest_framework import serializers

from .models import Payroll, SalaryPayment, CommissionPayment


class PayRollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payroll
        fields = ['user', 'monthly_salary',
                  'customers_brought', 'created_at', 'updated_at']


class SalaryPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalaryPayment
        fields = ['salary_employee_payment']


class CommissionPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommissionPayment
        fields = ['commission_employee_payemnt', 'commission_rate']
