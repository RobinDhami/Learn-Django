from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Student

# Create your views here.

def home(request):
    peoples = [
        {'name': 'Rabin Dhami', 'age': '27'},
        {'name': 'karan yogi', 'age': '17'},
        {'name': 'yogesh gwaje', 'age': '24'},
        {'name': 'Rabin kjjk', 'age': '20'}
    ]
    return render(request, "index.html", context={'peoples': peoples})

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("img")
        print(name)
        print(image)
        Student.objects.create(
            name=name,
            image=image,
        )
        return redirect('/login/')
    
    queryset = Student.objects.all()
    print(queryset)
    context = {"students": queryset}
    return render(request, 'signup.html', context)

