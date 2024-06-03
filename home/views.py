from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[{'name':'Rabin Dhami','age':'27'},
             {'name':'karan yogi','age':'17'},
             {'name':'yogesh gwaje','age':'24'},
             {'name':'Rabin kjjk','age':'20'}]
    return render (request,"index.html", context={'peoples':peoples})

def about(req):
    return render(req,'about.html')

def profile(req):
    return render(req,'profile.html')

def contact(req):
    return render(req,'contact.html')
