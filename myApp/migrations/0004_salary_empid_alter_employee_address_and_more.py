# Generated by Django 4.2.7 on 2023-11-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='EmpId',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emailId',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastName',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='salary',
            name='GrossSalary',
            field=models.TextField(max_length=8),
        ),
        migrations.AlterField(
            model_name='salary',
            name='TaxSlab',
            field=models.TextField(max_length=2),
        ),
        migrations.AlterField(
            model_name='salary',
            name='TotalSalary',
            field=models.TextField(max_length=8),
        ),
    ]
