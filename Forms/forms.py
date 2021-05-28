from django.forms import ModelForm
from .models import *
#from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email','password1', 'password2']
class DoctorForm(ModelForm):
	class Meta:
		model = Doctor
		fields = ['phone','medicalId']	
class DoctorProfileForm(ModelForm):
	class Meta:
		model = Doctor
		fields = '__all__'
		exclude = ['user']	
class ReceiptForm(ModelForm):
	class Meta:
		model = Receipt
		fields ='__all__'
		

class ReceiptTypeForm(ModelForm):
	class Meta:
		model = ReceiptType
		fields ='__all__'

class IncomeForm(ModelForm):
	class Meta:
		model = Income
		fields ='__all__'

class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields ='__all__'	

class SubTreatmentForm(ModelForm):
	class Meta:
		model = SubTreatment
		fields ='__all__'	

class TreatmentForm(ModelForm):
	class Meta:
		model = Treatment
		fields ='__all__'	

class ExpenseTypeForm(ModelForm):
	class Meta:
		model = ExpenseType
		fields ='__all__'

class IncomeTypeForm(ModelForm):
	class Meta:
		model = IncomeType
		fields ='__all__'

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields ='__all__'
				
class HospitalForm(ModelForm):
	class Meta:
		model = Hospital
		fields ='__all__'

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields ='__all__'