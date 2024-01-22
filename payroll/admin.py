from django.contrib import admin
from .models import Payroll, CommissionPayment, SalaryPayment

# Register your models here.

admin.site.register(Payroll)
admin.site.register(CommissionPayment)
admin.site.register(SalaryPayment)