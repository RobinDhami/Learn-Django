from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Learn concept of aggregate foreign key annotate learn how to play with data
class Student(models.Model):
    User= models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) #This is used to authenticate user
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="stud")
    email=models.EmailField(unique=True,default="")
    bio= models.TextField(blank=True)
    phone= models.CharField(max_length=20, null=True, blank=True) 

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__ (self)->str:
        return self.department
    class Meta:
        ordering= ['department']
    

class EmployeeID(models.Model):
    employee_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.employee_id

class Employee(models.Model):
    department = models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    employee_id = models.OneToOneField(EmployeeID,related_name='employeeid',on_delete=models.CASCADE)
    employee_name= models.CharField(max_length=100)
    employee_email = models.EmailField(unique=True)
    employee_age = models.IntegerField(default=18)
    employee_address = models.TextField

    def __str__(self) -> str:
        return self.employee_name
    
    class Meta:
        ordering = ['employee_name']
        verbose_name = "employee"
