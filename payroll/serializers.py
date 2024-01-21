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

class UserPayRollSerializer(serializers.ModelSerializer):

    monthly_salary = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Payroll
        fields = ['user', 'customers_brought', 'monthly_salary']

    def validate(self, attrs):
        user = attrs.get('user')

        if Payroll.objects.filter(user=user).exists():
            raise serializers.ValidationError('This user already has an existing payroll profile. Please review and, if needed, update the existing profile.')

        return attrs
