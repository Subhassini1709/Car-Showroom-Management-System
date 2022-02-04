from django.shortcuts import render
from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from users.models import *
from base64 import b64encode

@login_required(login_url='Login')
def home(request):
    return render(request, 'users/index.html')

def landing(request):
    return render(request, 'users/landing.html')

def about(request):
    return render(request, 'users/about.html')

def contact(request):
    return render(request, 'users/contact.html')

def register(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else:
            return redirect('Home Page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created successfully for '+user)
                return redirect('Login')

        context = {'form':form}
        return render(request, 'users/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else:
            return redirect('Home Page')
    else :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('/admin/')
                else:
                    login(request,user)
                    return redirect('Home Page')
            else:
                messages.info(request,'Username or Password is incorrect')
                

        context={}
        return render(request, 'users/login.html', context)



def logoutPage(request):
    logout(request)
    return redirect('Logout')

def buy(request):
    return render(request, 'users/buy.html')

def brand(request):
    brand_id = request.POST['brand_id']
    vehicles = BuyCar.objects.all()
    vehicle = vehicles.filter(BBrandID=brand_id)
    for i in vehicle:
        i.BCarImage = b64encode(i.BCarImage).decode()
    return render(request, 'users/brand_cars.html', {'vehicle':vehicle} )

def specs(request):
    car_id = request.POST['car_id']
    vehicles = BuySpecs.objects.all()
    vehicle = vehicles.filter(CarID=car_id)
    for i in vehicle:
        i.Image = b64encode(i.Image).decode()
    return render(request, 'users/car_specs.html', {'vehicle':vehicle} )

def buyform(request):
    return render(request, 'users/buy_form.html')

def buysuccess(request):
    return render(request, 'users/buy_success.html')

def rent(request):
    return render(request, 'users/rent.html')

def rentform(request):
    return render(request, 'users/rent_form.html')

def rentsuccess(request):
    return render(request, 'users/rent_success.html')

def sellform(request):
    return render(request, 'users/sell_form.html')

def sellsuccess(request):
    return render(request, 'users/sell_success.html')






