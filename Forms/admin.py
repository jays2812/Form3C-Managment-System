from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(SubTreatment)
admin.site.register(Treatment)
admin.site.register(ReceiptType)
admin.site.register(Receipt)
admin.site.register(Hospital)
admin.site.register(IncomeType)
admin.site.register(Income)
admin.site.register(ExpenseType)
admin.site.register(Expense)



