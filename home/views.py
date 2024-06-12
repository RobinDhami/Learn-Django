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
    queryset = Student.objects.all()
    print(queryset)
    context = {"students": queryset}
    print("context",context)
    return render(request, 'profile.html',context)

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("img")
        bio = request.POST.get("bio")
        email = request.POST.get("email")
        phone=request.POST.get("phone")

        Student.objects.create(
            name=name,
            image=image,
            bio=bio,
            email=email,
            phone = phone,
        )
        return redirect('/login/')
    
    return render(request, 'signup.html')
def delete_profile(request,id):
    queryset = Student.objects.get(id=id)
    queryset.delete()
    return redirect('/profile/')

def update_student(request, id):
    queryset = Student.objects.get(id=id)
    
    if request.method == 'POST':
        name = request.POST.get("name")
        image = request.FILES.get("img")
        bio = request.POST.get("bio")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        # Update the queryset with the new data
        queryset.name = name
        queryset.image = image
        queryset.bio = bio
        queryset.email = email
        queryset.phone = phone
        queryset.save()
        
    context = {"student": queryset}
    return render(request, 'update.html', context)
