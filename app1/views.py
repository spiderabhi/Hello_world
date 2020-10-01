from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        x = auth.authenticate(username=username, password=password)
        if x is None:
            return render(request, 'index.html',{'error':'Invalid Credential'})
        else:
            return redirect('Home')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        x = auth.authenticate(username=username, password=password)
        if x is None:
            return render(request, 'index.html')
        else:
            return redirect('Home')
    else:
        return redirect('/')


def signform(request):
    if request.method == 'POST':
        firstname = request.POST['First_Name']
        lastName = request.POST['Last_Name']
        username = request.POST['Username']
        password = request.POST['Password']
        contact = request.POST['Contact']
        email = request.POST['Email']
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastName, email=email,
                                     password=password)
        x.save()
        print("User Created")
        return redirect('/')
    else:
        return render(request, 'Loginform.html')


def home(request):
    return render(request, 'Home.html')
