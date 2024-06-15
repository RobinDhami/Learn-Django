from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.

def home(request):
    return render(request, "index.html")

@login_required(login_url='/login/')   #put the rout for where to redirect
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def profile(request):
    queryset = Student.objects.all()
    print(queryset)
    context = {"students": queryset}
    print("context",context)
    return render(request, 'profile.html',context)

@login_required(login_url='/login/')
def contact(request):
    return render(request, 'contact.html')

def AddData(request):
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
        return redirect('/profile/')
    
    return render(request, 'AddData.html')

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
        return redirect('/profile/')

    context = {"student": queryset}
    return render(request, 'update.html', context)

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the User Email already exists
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            messages.info(request, 'User with this email already exists')
            return redirect('/login/')  # Redirect back to registration page
        
        else:
            # Create a new User object
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
            )

            # Set the password using set_password() method
            user.set_password(password)
            
            # Save the user object to the database
            user.save()
            messages.success(request, 'Account added successfully')
            
            # Redirect to login page after successful registration
            return redirect('/login/')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('profile')  
        else:
            messages.error(request, 'Invalid credentials')

    # If GET request or authentication failed, render the login form
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('profile')