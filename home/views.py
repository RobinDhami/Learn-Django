from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[{'name':'Rabin Dhami','age':'27','image': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D'},]
            #  {'name':'karan yogi','age':'17'},
            #  {'name':'yogesh gwaje','age':'24'},
            #  {'name':'Rabin kjjk','age':'20'}]
    return render (request,"index.html", context={'peoples':peoples})

