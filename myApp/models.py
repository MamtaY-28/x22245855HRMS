"""
This module provides functionality related to Product,Contact Us,Employee,salary.

Author: Mamta Yadav
Date: 6-12-2024
"""
from django.db import models
# check for coomit


class ContactUs(models.Model):
    """
    Model representing a contact us entry.

    Attributes:
        ContactId (AutoField): Primary key for the contact entry.
        Name (TextField): Name of the contact person.
        Email (TextField): Email address of the contact person.
        ContactNumber (TextField): Contact number of the person.
        CompnayName (TextField): Name of the company.
        Message (TextField): Message from the contact person.
        created_at (DateTimeField): Timestamp of when the entry was created.
    """
    ContactId = models.AutoField(primary_key=True)
    Name = models.TextField(max_length=40)
    Email = models.TextField(max_length=10, null=True)
    ContactNumber = models.TextField(max_length=10)
    CompnayName = models.TextField(max_length=10)
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ContactId)

class Employee(models.Model):
    """
    Model representing an employee.

    Attributes:
        EmpId (AutoField): Primary key for the employee.
        firstName (TextField): First name of the employee.
        middleName (TextField): Middle name of the employee (nullable).
        lastName (TextField): Last name of the employee.
        emailId (TextField): Email address of the employee.
        mobileNumber (TextField): Mobile number of the employee.
        gender (CharField): Gender of the employee (choices: 'M', 'F', 'O').
        DOB (TextField): Date of birth of the employee.
        address (TextField): Address of the employee.
        password (TextField): Password for the employee.
        created_at (DateTimeField): Timestamp of when the employee record was created.
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Unisex'),
    )

    EmpId = models.AutoField(primary_key=True)
    firstName = models.TextField(max_length=40)
    middleName = models.TextField(max_length=10, blank=True)
    lastName = models.TextField()
    emailId = models.TextField()
    mobileNumber = models.TextField()
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    DOB = models.TextField(max_length=40)
    address = models.TextField()
    password = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.EmpId)

class Salary(models.Model):
    """
    Model representing salary details.

    Attributes:
        SalaryId (AutoField): Primary key for the salary entry.
        EmpId (TextField): Employee ID associated with the salary (nullable).
        MonthlySalary (TextField): Monthly salary amount.
        TotalSalary (TextField): Total salary amount.
        GrossSalary (TextField): Gross salary amount.
        TaxSlab (TextField): Tax slab information.
        created_at (DateTimeField): Timestamp of when the entry was created.
    """
    SalaryId = models.AutoField(primary_key=True)
    EmpId = models.TextField(blank=True)
    MonthlySalary = models.TextField(max_length=40)
    TotalSalary = models.TextField(max_length=8)
    GrossSalary = models.TextField(max_length=8)
    TaxSlab = models.TextField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.EmpId)