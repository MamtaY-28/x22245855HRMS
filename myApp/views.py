# from imp
from django.shortcuts import render
from myApp.models import Employee
from myApp.models import Salary
from django.http import HttpResponseRedirect
from django.contrib import messages     
#Home
def home(request):
    return render(request,'home.html')

#Add Contact Us Details

def ContactUs(request):
    if request.method=='POST':
        if request.POST.get('Name') \
          and request.POST.get('Email') \
          and request.POST.get('ContactNumber') \
          and request.POST.get('CompnayName') \
          and request.POST.get('Message') :
          ContactUs=ContactUs()
          ContactUs.Name=request.POST.get('Name')
          ContactUs.Email=request.POST.get('Email')
          ContactUs.ContactNumber=request.POST.get('ContactNumber')
          ContactUs.CompnayName=request.POST.get('CompnayName')
          ContactUs.Message=request.POST.get('Message')
          ContactUs.save()
          messages.success(request,"Thanks For Contacting. Will Contact you soon !")
        return render(request,'contactusForm.html')
    else:
         return render(request,'contactusForm.html')            


#Add Employee

#View All Employee List
def EmployeeList(request):
    all_employee=Employee.objects.all().order_by('-created_at')
    return render(request,'EmployeeList.html',{"employees":all_employee})

#Add Employee
def add_employee(request):
    if request.method=='POST':
        if request.POST.get('firstName') \
          and request.POST.get('middleName') \
          and request.POST.get('lastName') \
          and request.POST.get('emailId') \
          and request.POST.get('mobileNumber') \
          and request.POST.get('gender') \
          and request.POST.get('DOB') \
          or request.POST.get('address') \
          or request.POST.get('password') :
          employee=Employee()
          employee.firstName=request.POST.get('firstName')
          employee.middleName=request.POST.get('middleName')
          employee.lastName=request.POST.get('lastName')
          employee.emailId=request.POST.get('emailId')
          employee.mobileNumber=request.POST.get('mobileNumber')
          employee.gender=request.POST.get('gender')
          employee.DOB=request.POST.get('DOB')
          employee.address=request.POST.get('address')
          employee.password=request.POST.get('password')          
          employee.save()
          messages.success(request,"EmployeeList added successfully !")
          return render(request,'EmployeeList.html',{"employees":Employee.objects.all().order_by('-created_at')})
    else:
         return render(request,'AddEmployee.html')            


#View the product individually
def employee(request,EmpId):
    employee=Employee.objects.get(EmpId=EmpId)
    if employee!=home:
        return render(request,'EditEmployee.html',{'employee':employee})

#Edit Employee
def edit_employee(request):
    if request.method=='POST':
        employee=Employee.objects.get(EmpId=request.POST.get('EmpId'))
        if employee!=home:
            employee.firstName=request.POST.get('firstName')
            employee.middleName=request.POST.get('middleName')
            employee.lastName=request.POST.get('lastName')
            employee.emailId=request.POST.get('emailId')
            employee.mobileNumber=request.POST.get('mobileNumber')
            employee.gender=request.POST.get('gender')
            employee.DOB=request.POST.get('DOB')
            employee.address=request.POST.get('address')
            employee.password=request.POST.get('password') 
            employee.save()
            messages.success(request,"employee updated successfully !")
            return render(request,'EmployeeList.html',{"employees":Employee.objects.all().order_by('-created_at')})
  
#Delete Employee
def delete_employee(request,EmpId):
    product=Employee.objects.get(EmpId=EmpId)
    product.delete()
    messages.success(request,"employee deleted successfully !")
    return render(request,'EmployeeList.html',{"employees":Employee.objects.all().order_by('-created_at')})
  
#View All Product List
def SalaryList(request):
    all_salary=Salary.objects.all().order_by('-created_at')
    return render(request,'SalaryList.html',{"salarys":all_salary})

#Add salary
def add_salary(request):
    if request.method=='POST':
        if request.POST.get('EmpId') \
          and request.POST.get('MonthlySalary') \
          and request.POST.get('TotalSalary') \
          and request.POST.get('GrossSalary') \
          and request.POST.get('TaxSlab') :
          
          salary=Salary()
          salary.EmpId=request.POST.get('EmpId')
          salary.MonthlySalary=request.POST.get('MonthlySalary')
          salary.TotalSalary=request.POST.get('TotalSalary')
          salary.GrossSalary=request.POST.get('GrossSalary')
          salary.TaxSlab=request.POST.get('TaxSlab')
          salary.save()
          messages.success(request,"Salary added successfully !")
          return render(request,'SalaryList.html',{"salarys":Salary.objects.all().order_by('-created_at')})
    else:
         return render(request,'AddSalary.html')            

#View the product individually
def salary(request,SalaryId):
    salary=Salary.objects.get(SalaryId=SalaryId)
    if salary!=home:
        return render(request,'EditSalary.html',{'salary':salary})

#Edit Product
def edit_salary(request):
    if request.method=='POST':
        salary=Salary.objects.get(SalaryId=request.POST.get('SalaryId'))
        if salary!=home:
          salary.EmpId=request.POST.get('EmpId')
          salary.MonthlySalary=request.POST.get('MonthlySalary')
          salary.TotalSalary=request.POST.get('TotalSalary')
          salary.GrossSalary=request.POST.get('GrossSalary')
          salary.TaxSlab=request.POST.get('TaxSlab')
          salary.save()
          messages.success(request,"Salary updated successfully !")
          return render(request,'SalaryList.html',{"salarys":Salary.objects.all().order_by('-created_at')})
  
#Delete product
def delete_salary(request,SalaryId):
    product=Salary.objects.get(SalaryId=SalaryId)
    product.delete()
    messages.success(request,"salary deleted successfully !")
    return render(request,'SalaryList.html',{"salarys":Salary.objects.all().order_by('-created_at')})