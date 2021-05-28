from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
	user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
	phone = models.CharField(max_length=200, null=True,blank=True)
	email = models.CharField(max_length=200, null=True,blank=True)
	medicalId = models.CharField(max_length=10, null=True,blank=True)
	profile_pic = models.ImageField(default="profile1.png",null=True, blank=True)

	def __str__(self):
		return self.user.username

class Hospital(models.Model):
	hospital_name = models.CharField(max_length=50, null=True)
	doctor = models.ForeignKey(Doctor, null=True, on_delete =models.SET_NULL)
	printline1 = models.CharField(max_length=200, null=True)
	printline2 = models.CharField(max_length=200, null=True)
	printline3 = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.hospital_name

class Patient(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	age = models.FloatField(null=True)
	gender = models.CharField(max_length=6,null=True)
	doctor = models.ForeignKey(Doctor, null=True, on_delete = models.SET_NULL)
	hospital_name = models.ForeignKey(Hospital, null=True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.name

class SubTreatment(models.Model):
	sub_treatment = models.CharField(max_length=200, null=True)
	rate = models.FloatField(null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.sub_treatment

class Treatment(models.Model):
	treatment = models.CharField(max_length=50, null=True)
	#sub_treatment = models.ManyToManyField(SubTreatment)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.treatment

class ReceiptType(models.Model):
	name = models.CharField(max_length=200, null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.name

class Receipt(models.Model):
	name = models.ForeignKey(ReceiptType, null=True, on_delete =models.SET_NULL)
	doctor = models.ForeignKey(Doctor, null=True, on_delete =models.SET_NULL)
	treatment = models.ForeignKey(Treatment, null=True, on_delete =models.SET_NULL)
	subtreatment = models.ForeignKey(SubTreatment, null=True, on_delete =models.SET_NULL)
	patient = models.ForeignKey(Patient, null=True, on_delete =models.SET_NULL)
	date = models.DateTimeField(auto_now_add=True, null=True)
	amount = models.FloatField(null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.patient.name


class IncomeType(models.Model):
	name = models.CharField(max_length=200, null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.name

class Income(models.Model):
	Iname = models.ForeignKey(IncomeType, null=True, on_delete =models.SET_NULL)
	doctor = models.ForeignKey(Doctor, null=True, on_delete =models.SET_NULL)
	date = models.DateTimeField(auto_now_add=True, null=True)
	amount = models.FloatField(null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.Iname.name

class ExpenseType(models.Model):
	name = models.CharField(max_length=200, null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.name

class Expense(models.Model):
	Ename = models.ForeignKey(ExpenseType, null=True, on_delete =models.SET_NULL)
	doctor = models.ForeignKey(Doctor, null=True, on_delete =models.SET_NULL)
	date = models.DateTimeField(auto_now_add=True, null=True)
	amount = models.FloatField(null=True)
	remarks = models.CharField(max_length=200, null=True, blank = True)

	def __str__(self):
		return self.Ename.name

class Feedback(models.Model):
	FeedbackType = models.CharField(max_length=10, null=True)
	FeedbackDescription = models.CharField(max_length=200, null=True)
	Email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.Email
# Create your models here.
