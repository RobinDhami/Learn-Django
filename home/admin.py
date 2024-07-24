from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(EmployeeID)
admin.site.register(Employee)