"""
URL configuration for HRMSProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('',views.home,name='home'),
    #EmployeeList
    path('EmployeeList',views.EmployeeList,name='EmployeeList'),    
    #Add Employee
    path('add_employee',views.add_employee,name='add_employee'),
    # #View Employee individually
    path('employee/<str:EmpId>',views.employee,name='employee'),
    #Edit Employee
    path('edit_employee',views.edit_employee,name='edit_employee'),
    # #Delete Employee
    path('delete_employee/<str:EmpId>',views.delete_employee,name='employee'),

    #SalaryList
    path('SalaryList',views.SalaryList,name='SalaryList'),    
    #Add Salary
    path('add_salary',views.add_salary,name='add_salary'),
    # #View Salary individually
    path('salary/<str:SalaryId>',views.salary,name='salary'),
    #Edit salary
    path('edit_salary',views.edit_salary,name='edit_salary'),
    # #Delete salary
    path('delete_salary/<str:SalaryId>',views.delete_salary,name='delete_salary'),
    # #Delete ContactUs
    path('ContactUs',views.ContactUs,name='ContactUs')
]
