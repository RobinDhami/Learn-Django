from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="stud")
    email=models.EmailField(unique=True,default="")
    bio= models.TextField(blank=True)
    phone= models.CharField(max_length=20, null=True, blank=True)  
