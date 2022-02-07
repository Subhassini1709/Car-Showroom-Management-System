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
    if request.method=='POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['mobile']
        message = request.POST['comments']
        ins = Contact(CFname=fname,CLname=lname, CEmail=email, CPhone=phone, CMessage=message)
        ins.save()  
        return redirect('ContactSuccess')
    return render(request, 'users/contact.html')

def contactsuccess(request):
    return render(request, 'users/contact_success.html')


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
                messages.success(
                    request, 'Account created successfully for '+user)
                return redirect('Login')

        context = {'form': form}
        return render(request, 'users/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else:
            return redirect('Home Page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('/admin/')
                else:
                    login(request, user)
                    return redirect('Home Page')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('Logout')


def buy(request):
    return render(request, 'users/buy.html')

def buydump(request):
    car_id = request.POST['cid']
    vehicles = BuyCar.objects.all()
    vehicle = vehicles.filter(BCarID=car_id)
    vs = BuyCar.objects.get(BCarID=car_id)
        
    return render(request, 'users/buy_form.html', {'vehicle': vehicle, 'vs':vs})


def brand(request):
    brand_id = request.POST['brand_id']
    vehicles = BuyCar.objects.all()
    vehicle = vehicles.filter(BBrandID=brand_id)
    for i in vehicle:
        i.BCarImage = b64encode(i.BCarImage).decode()
    return render(request, 'users/brand_cars.html', {'vehicle': vehicle})


def specs(request):
    car_id = request.POST['car_id']
    vehicles = BuySpecs.objects.all()
    vehicle = vehicles.filter(CarID=car_id)
    for i in vehicle:
        i.Image = b64encode(i.Image).decode()
    return render(request, 'users/car_specs.html', {'vehicle': vehicle})


def buyform(request):
    if request.method == "POST":
        x = request.POST['carid']
        carid = BuyCar.objects.get(BCarID=x)
        y = request.POST['brandid']
        brandid = BuyBrand.objects.get(BrandID=y)
        customerid = request.user
        address = request.POST['address']
        phone = request.POST['phone']
        ins = BuyBooking(BCarID=carid, BBrandID=brandid, BCustomerID=customerid, BAddress=address, BPhoneNumber=phone)
        ins.save()
        return redirect('BuySuccess')
    return render(request, 'users/buy_form.html')

    
def buysuccess(request):
    bookid = BuyBooking.objects.order_by('-id')[0]
    bookdetails = BuyBooking.objects.all()
    bookdetail = bookdetails.filter(id=bookid.id)
    b = BuyBooking.objects.get(id=bookid.id)
    costs = BuySpecs.objects.all()
    cost = costs.filter(CarID_id=b.BCarID) 
    return render(request, 'users/buy_success.html',{'bookdetail':bookdetail, 'cost':cost})

def rent(request):
    vehicles = RentCar.objects.all()
    for i in vehicles:
        i.RImage = b64encode(i.RImage).decode()
    return render(request, 'users/rent.html',{'vehicles':vehicles})

def rentform(request):
    vehicles = RentCar.objects.all()
    if request.method=='POST':
        customerid = request.user
        carname = request.POST['cars']
        carid = RentCar.objects.get(RCarName=carname)
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        days = request.POST['days']
        rent = carid.RCarPrice
        phone = request.POST['phone']
        address = request.POST['address']
        ins = RentBooking(RCustomerID=customerid, RCarID=carid, FromDate=fromdate, ToDate=todate,NoOfDays=days, RentPerDay=rent, RPhoneNum=phone, RAddress=address)
        ins.save()  
        return redirect('RentSuccess')
    return render(request, 'users/rent_form.html',{'vehicles':vehicles})

def rentsuccess(request):
    rentid = RentBooking.objects.order_by('-id')[0]
    rentdetails = RentBooking.objects.all()
    rentdetail = rentdetails.filter(id=rentid.id)
    return render(request, 'users/rent_success.html',{'rentdetail':rentdetail})

def sellform(request):
    if request.method=='POST':
        customerid = request.user
        brand = request.POST['brand']
        carname = request.POST['carname']
        price = request.POST['price']
        km = request.POST['km']
        age = request.POST['age']
        fuel = request.POST['fuel']
        mileage = request.POST['mileage']
        seating = request.POST['seating']
        phone = request.POST['phone']
        address = request.POST['address']
        ins = SellCar(SCustomerID=customerid,SBrandName=brand, SCarName=carname, SCarPrice=price, KmRun=km, CarAge=age, SFuel=fuel, SMileage=mileage, SSeatingCapacity=seating, SPhoneNum=phone, SAddress=address)
        ins.save()  
        return redirect('SellSuccess')
    return render(request, 'users/sell_form.html')

def sellsuccess(request):
    sellid = SellCar.objects.order_by('-id')[0]
    selldetails = SellCar.objects.all()
    selldetail = selldetails.filter(id=sellid.id)
    return render(request, 'users/sell_success.html',{'selldetail':selldetail})






