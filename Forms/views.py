from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users
from .filters import *
from datetime import date

import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def start(request):
	doctors = Doctor.objects.all()
	context = {'doctors':doctors}
	return render(request,'Forms/start.html',context)

#@unauthenticated_user
def RegisterPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.save()
			#doctor=doctor.save()
			#username = form.cleaned_data.get('username')
			#messages.success(request, 'Account was created for ' + user)
			group = Group.objects.get(name='doctor')
			user.groups.add(group)
			Doctor.objects.create(
			user=user
			)
			return redirect('login')
			

	context = {'form':form}
	return render(request, 'Forms/register.html', context)
		
@login_required(login_url='login')
def CreatePatient(request,pk):
	doctor = Doctor.objects.get(id=pk)
	hname = doctor.hospital_set.all()
	if request.method == "POST":  
		form=PatientForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = PatientForm(initial={'doctor':doctor,'hospital_name':hname})  
	return render(request,'Forms/Patient.html',{'form':form})

@login_required(login_url='login')
def CreateExpenseType(request):
	if request.method == "POST":  
		form=ExpenseTypeForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = ExpenseTypeForm()  
	return render(request,'Forms/ExpenseType.html',{'form':form})	

@login_required(login_url='login')
def CreateExpenseForm(request,pk):
	doctor = Doctor.objects.get(id=pk)
	if request.method == "POST":  
		form=ExpenseForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = ExpenseForm(initial={'doctor':doctor})
	return render(request,'Forms/ExpenseForm.html',{'form':form})

@login_required(login_url='login')
def CreateReceiptType(request):
	if request.method == "POST":  
		form=ReceiptTypeForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = ReceiptTypeForm()  
	return render(request,'Forms/ReceiptType.html',{'form':form})

@login_required(login_url='login')
def CreateHospitalForm(request):
	doctor = request.user.doctor
	if request.method == "POST": 
		form=HospitalForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = HospitalForm(initial={'doctor':doctor})  
	context = {'form':form}	
	return render(request,'Forms/HospitalForm.html',context)

@login_required(login_url='login')
def UpdateHospital(request, pk):
	ViewHospital = Hospital.objects.get(id=pk)
	form = HospitalForm(instance = ViewHospital)

	if request.method == 'POST':
		form = HospitalForm(request.POST,instance = ViewHospital)
		if form.is_valid():
			form.save()
			return redirect('/ViewHospital/')

	context = {'form':form}
	return render(request, 'Forms/UpdateReceipt.html', context)	


@login_required(login_url='login')
def CreateIncomeType(request):
	if request.method == "POST":  
		form=IncomeTypeForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = IncomeTypeForm()  
	return render(request,'Forms/IncomeType.html',{'form':form})

@login_required(login_url='login')
def CreateIncomeForm(request,pk):
	doctor = Doctor.objects.get(id=pk)
	if request.method == "POST":  
		form=IncomeForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = IncomeForm(initial={'doctor':doctor})  
	return render(request,'Forms/IncomeForm.html',{'form':form})

@login_required(login_url='login')
def CreateReceiptForm(request,pk):
	doctor = Doctor.objects.get(id=pk)
	patients = doctor.patient_set.all()
	if request.method == "POST": 
		form=ReceiptForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = ReceiptForm(initial={'doctor':doctor,'patient':patients})  
	context = {'form':form}	
	return render(request,'Forms/ReceiptForm.html',context)

@login_required(login_url='login')
def UpdateReceipt(request, pk):
	viewreceipt= Receipt.objects.get(id=pk)
	form = ReceiptForm(instance = viewreceipt)

	if request.method == 'POST':
		form = ReceiptForm(request.POST,instance = viewreceipt)
		if form.is_valid():
			form.save()
			return redirect('/ViewReceipt/')

	context = {'form':form}
	return render(request, 'Forms/UpdateReceipt.html', context)	

@login_required(login_url='login')
def PatientHistory(request):
	patients = request.user.doctor.patient_set.all()
	receipt = request.user.doctor.receipt_set.all()
	myFilter = PatientFilter(request.GET, queryset=patients)
	patients = myFilter.qs 
	context = {'patient':patients,'receipt':receipt,'myFilter':myFilter}
	response = render(request,'Forms/PatientHistory.html',context)
	return response	

@login_required(login_url='login')
def CreateSubTreatmentForm(request):
	if request.method == "POST":  
		form=SubTreatmentForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = SubTreatmentForm()  
	return render(request,'Forms/SubTreatmentForm.html',{'form':form})

@login_required(login_url='login')
def CreateTreatmentForm(request):
	if request.method == "POST":  
		form=TreatmentForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = TreatmentForm()  
	return render(request,'Forms/TreatmentForm.html',{'form':form})

@login_required(login_url='login')
def ViewExpenseType(request):
	ViewExpenseType = ExpenseType.objects.all()
	context =  {'ViewExpenseType':ViewExpenseType}
	response = render(request,'Forms/ViewExpenseType.html',context)
	return response

@login_required(login_url='login')
def ViewExpense(request):
	ViewExpense = request.user.doctor.expense_set.all()
	context =  {'ViewExpense':ViewExpense}
	response = render(request,'Forms/ViewExpense.html',context)
	return response

@login_required(login_url='login')
def ViewTodayExpense(request):
	ViewExpense = request.user.doctor.expense_set.filter(date__date=date.today())
	context =  {'ViewExpense':ViewExpense}
	response = render(request,'Forms/ViewExpense.html',context)
	return response	

def ViewExpenseTypewise(request):
	ViewExpenseTypewise = request.user.doctor.expense_set.all()
	myFilter = TypewiseExpenseFilter(request.GET, queryset=ViewExpenseTypewise)
	ViewExpenseTypewise = myFilter.qs 
	context =  {'ViewExpenseTypewise':ViewExpenseTypewise,
				'myFilter':myFilter
				}
	response = render(request,'Forms/ViewExpenseTypewise.html',context)
	return response

@login_required(login_url='login')
def ViewHospital(request):
	ViewHospital = request.user.doctor.hospital_set.all()
	context =  {'ViewHospital':ViewHospital}
	response = render(request,'Forms/ViewHospital.html',context)
	return response



@login_required(login_url='login')
def ViewIncome(request):
	ViewIncome = request.user.doctor.income_set.all()
	context =  {'ViewIncome':ViewIncome}
	response = render(request,'Forms/ViewIncome.html',context)
	return response

@login_required(login_url='login')
def ViewTodayIncome(request):
	ViewIncome = request.user.doctor.income_set.filter(date__date=date.today())
	context =  {'ViewIncome':ViewIncome}
	response = render(request,'Forms/ViewIncome.html',context)
	return response	

@login_required(login_url='login')
def ViewIncomeType(request):
	ViewIncomeType = IncomeType.objects.all()
	context =  {'ViewIncomeType':ViewIncomeType}
	response = render(request,'Forms/ViewIncomeType.html',context)
	return response

@login_required(login_url='login')
def ViewIncomeTypewise(request):
	ViewIncomeTypewise = request.user.doctor.income_set.all()
	myFilter = TypewiseIncomeFilter(request.GET, queryset=ViewIncomeTypewise)
	ViewIncomeTypewise = myFilter.qs 
	context =  {'ViewIncomeTypewise':ViewIncomeTypewise,
				'myFilter':myFilter
				}
	response = render(request,'Forms/ViewIncomeTypewise.html',context)
	return response

@login_required(login_url='login')
def ViewReceipt(request):
	ViewReceipt = request.user.doctor.receipt_set.all()
	print(ViewReceipt)
	context =  {'ViewReceipt':ViewReceipt}
	response = render(request,'Forms/ViewReceipt.html',context)
	return response

@login_required(login_url='login')
def ViewTodayReceipt(request):
	ViewReceipt = request.user.doctor.receipt_set.filter(date__date=date.today())
	context =  {'ViewReceipt':ViewReceipt}
	response = render(request,'Forms/ViewReceipt.html',context)
	return response	

@login_required(login_url='login')
def ViewFinancialReceipt(request):
	ViewFinancialReceipt= request.user.doctor.receipt_set.all()
	myFilter = FinancialFilter(request.GET, queryset=ViewFinancialReceipt)
	ViewFinancialReceipt = myFilter.qs 
	context =  {'ViewFinancialReceipt':ViewFinancialReceipt,
				'myFilter':myFilter
				}
	response = render(request,'Forms/ViewFinancialReceipt.html',context)
	return response	

@login_required(login_url='login')
def ViewPrintReceipt(request):
	ViewPrintReceipt = request.user.doctor.receipt_set.all()
	context =  {'ViewPrintReceipt':ViewPrintReceipt}
	response = render(request,'Forms/ViewPrintReceipt.html',context)
	return response	

@login_required(login_url='login')
def ViewReceiptType(request):
	ViewReceiptType = ReceiptType.objects.all()
	context =  {'ViewReceiptType':ViewReceiptType}
	response = render(request,'Forms/ViewReceiptType.html',context)
	return response

@login_required(login_url='login')
def ViewReceiptTreatment(request):
	ViewReceiptTreatment = Receipt.objects.all()
	myFilter = TreatmentFilter(request.GET, queryset=ViewReceiptTreatment)
	ViewReceiptTreatment = myFilter.qs 
	context =  {'ViewReceiptTreatment':ViewReceiptTreatment,
				'myFilter':myFilter
				}
	response = render(request,'Forms/ViewReceiptTreatment.html',context)
	return response

@login_required(login_url='login')
def ViewSubTreatment(request):
	ViewSubTreatment = SubTreatment.objects.all()
	context =  {'ViewSubTreatment':ViewSubTreatment}
	response = render(request,'Forms/ViewSubTreatment.html',context)
	return response


@login_required(login_url='login')
def ViewTreatment(request):
	ViewTreatment = Treatment.objects.all()
	context =  {'ViewTreatment':ViewTreatment}
	response = render(request,'Forms/ViewTreatment.html',context)
	return response



def ViewResearch(request):
	ViewResearch = Receipt.objects.all()
	myFilter = ReceiptFilter(request.GET, queryset=ViewResearch)
	ViewResearch = myFilter.qs 
	context =  {'ViewResearch': ViewResearch,'myFilter':myFilter}
	response = render(request,'Forms/ViewResearch.html',context)
	return response

def doctor(request, pk_test):
	doctors = Doctor.objects.get(id=pk_test)
	context={'doctors':doctors}
	return render(request,'Forms/doctor.html',context)

@login_required(login_url='login')
def ViewProfile(request):
	doctor = request.user.doctor
	ViewHospital = request.user.doctor.hospital_set.all()
	form = DoctorProfileForm(instance=doctor)
	if request.method == 'POST':
		form = DoctorProfileForm(request.POST, request.FILES,instance=doctor)
		if form.is_valid():
			form.save()
	context = {'form':form,'hospital':ViewHospital}
	return render(request, 'Forms/profile.html',context)


@login_required(login_url='login')
def home(request):
	doctor = request.user.doctor
	context ={'doctor':doctor}
	return render(request,'Forms/homepage.html',context)

@login_required(login_url='login')
def aboutus(request):
	return render(request,'Forms/aboutus.html')	

@login_required(login_url='login')
def disclaimer(request):
	return render(request,'Forms/disclaimer.html')

@login_required(login_url='login')
def feedback(request):
	if request.method == "POST":  
		form=feedback(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/home')  
			except:  
				pass  
	else:  
		form = FeedbackForm()  
	return render(request,'Forms/feedback.html',{'form':form})

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf(request,pk):
    receipt=Receipt.objects.get(id=pk)
    ViewHospital = request.user.doctor.hospital_set.all()
    
    dict={
        'ReceiptType':receipt.name,
        'Doctor':receipt.doctor,
        'Treatment':receipt.treatment,
        'Date':receipt.date,
        'SubTreatment':receipt.subtreatment,
        'Remarks':receipt.remarks,
        'Name':receipt.patient,
        'Total_Charge':receipt.amount,
        'Hospital':ViewHospital,
    }
    return render_to_pdf('Forms/download_bill.html',dict)	

# def profile(request):
#	return render(request, 'users/profile.html')	

# Create your views here.
