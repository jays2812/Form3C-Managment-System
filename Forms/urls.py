from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	path('',views.start,name='form-start'),
    path('doctor/<int:pk_test>/',views.doctor,name='doctor'),
    path('home/',views.home,name='form-home'),
    path('login/',auth_views.LoginView.as_view(template_name='Forms/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Forms/logout.html'), name='logout'),
    path('Register/',views.RegisterPage,name='form-register'),
    path('profile/',views.ViewProfile,name='profile'),
    path('ExpenseTypeForm/',views.CreateExpenseType,name='form-expensetype'),
    path('ExpenseForm/<int:pk>/',views.CreateExpenseForm,name='form-expense'),
    path('ViewExpenseTypewise/',views.ViewExpenseTypewise,name='form-view-expense-typewise'),
    path('IncomeTypeForm/',views.CreateIncomeType,name='form-incometype'),
    path('IncomeForm/<int:pk>/',views.CreateIncomeForm,name='form-income'),
    path('ViewIncomeTypewise/',views.ViewIncomeTypewise,name='form-view-income-typewise'),
    path('HospitalForm/',views.CreateHospitalForm,name='form-hospital'),
    path('UpdateHospital/<int:pk>/',views.UpdateHospital,name='update-hospital'),
    path('ReceiptForm/<int:pk>/',views.CreateReceiptForm,name='form-createreceipt'),
    path('UpdateReceipt/<str:pk>/',views.UpdateReceipt,name='form-update-receipt'),
    path('ReceiptTypeForm/',views.CreateReceiptType,name='form-receipttype'),
    path('ViewReceiptTreatment/',views.ViewReceiptTreatment,name='form-view-receipt-treatment'),
    path('TreatmentForm/',views.CreateTreatmentForm,name='form-treatment'),
    path('SubTreatmentForm/',views.CreateSubTreatmentForm,name='form-subtreatment'),
    path('PatientForm/<int:pk>/',views.CreatePatient,name='form-createpatient'),
    path('ViewExpense/',views.ViewExpense,name='form-view-expense'),
    path('DailyExpense/',views.ViewTodayExpense,name='daily-expense'),
    path('ViewExpenseType/',views.ViewExpenseType,name='form-view-expense-type'),
    path('ViewIncome/',views.ViewIncome,name='form-view-income'),
    path('DailyIncome/',views.ViewTodayIncome,name='daily-income'),
    path('ViewIncomeType/',views.ViewIncomeType,name='form-view-income-type'),
    path('ViewHospital/',views.ViewHospital,name='form-view-hospital'),
    path('ViewReceipt/',views.ViewReceipt,name='form-view-receipt'),
    path('DailyReceipt/',views.ViewTodayReceipt,name='daily-receipt'),
    path('FinancialReceipt/',views.ViewFinancialReceipt,name='financial-receipt'),
    path('PrintReceipt/',views.ViewPrintReceipt,name='form-print-receipt'),
    path('DownloadReceipt/<int:pk>',views.download_pdf,name='form-download-receipt'),
    path('ViewReceiptType/',views.ViewReceiptType,name='form-view-receipt-type'),
    path('ViewResearch/',views.ViewResearch,name='form-view-research'),
    path('ViewTreatment/',views.ViewTreatment,name='form-view-treatment'),
    path('ViewSubTreatment/',views.ViewSubTreatment,name='form-view-subtreatment'),
    path('PatientHistory/',views.PatientHistory,name='patient-history'),
    path('AboutUs/',views.aboutus,name='form-about'),
    path('Disclaimer/',views.disclaimer,name='form-disclaimer'),
    path('Feedback/',views.feedback,name='form-feedback'),
#    path('profile/',views.profile,name='profile'),
    
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)