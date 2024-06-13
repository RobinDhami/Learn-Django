from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    User= models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) #This is used to authenticate user
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="stud")
    email=models.EmailField(unique=True,default="")
    bio= models.TextField(blank=True)
    phone= models.CharField(max_length=20, null=True, blank=True)  
