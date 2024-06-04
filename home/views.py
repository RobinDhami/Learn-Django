from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[{'name':'Rabin Dhami','age':'27'},
             {'name':'karan yogi','age':'17'},
             {'name':'yogesh gwaje','age':'24'},
             {'name':'Rabin kjjk','age':'20'}]
    return render (request,"index.html", context={'peoples':peoples})

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request,'profile.html')

def contact(request):
    return render(request,'contact.html')
