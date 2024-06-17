# Generated by Django 5.0.6 on 2024-06-17 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_email', models.EmailField(max_length=254, unique=True)),
                ('employee_age', models.IntegerField(default=18)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='home.department')),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employeeid', to='home.employeeid')),
            ],
            options={
                'verbose_name': 'employee',
                'ordering': ['employee_name'],
            },
        ),
    ]
