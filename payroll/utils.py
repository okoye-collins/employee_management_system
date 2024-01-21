# from 
from .models import CommissionPayment, SalaryPayment
# from 

class PayrollService:
    @staticmethod
    def calculate_salary(data):
        user = data['user']
        customers_brought = data['customers_brought']
        if user.employee_type == 'Salary':
            salary = SalaryPayment.objects.all().exists()
            if salary:
                salary = SalaryPayment.objects.all().first().salary_employee_payment
                return salary
            else:
                return 0
        elif user.employee_type == 'Commission':
            salary = CommissionPayment.objects.all().exists()
            if salary:
                salary = CommissionPayment.objects.all().first()
                commission_salary = salary.commission_employee_payemnt
                commission_rate = salary.commission_rate
                total_salary = commission_salary + (commission_rate * customers_brought)
                return total_salary
            else:
                return 0
        else:
            return 0
