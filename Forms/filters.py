import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ReceiptFilter(django_filters.FilterSet):
	#start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	#end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	#note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Receipt
		fields = '__all__'
		exclude = ['doctor', 'amount','patient','name']

class TreatmentFilter(django_filters.FilterSet):
	"""docstring for TreatementFilter"""
	class Meta:
		model = Receipt
		fields ='__all__'
		exclude = ['name','doctor','amount','remarks', 'patient']


class TypewiseExpenseFilter(django_filters.FilterSet):
	"""docstring for TypewiseExpenseFilter"""
	class Meta:
		model = Expense
		fields ='__all__'
		exclude = ['doctor','amount','remarks']
			
class TypewiseIncomeFilter(django_filters.FilterSet):
	"""docstring for TypewiseExpenseFilter"""
	class Meta:
		model = Income
		fields ='__all__'
		exclude = ['doctor','amount','remarks']		

class FinancialFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	#note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Receipt
		fields = '__all__'
		exclude = ['doctor','amount','patient','name','treatment','subtreatment','date','remarks']

class PatientFilter(django_filters.FilterSet):
	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['age','doctor','hospital_name','gender']		