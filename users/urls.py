from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='Landing'),
    path('home/',views.home, name='Home Page'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    
    path('login/', views.loginPage, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='Logout'),

    path('buy/', views.buy, name='Buy'),
    path('buy_dump/',views.buydump, name='BuyDump'),
    path('brand/', views.brand, name='Brand'), 
    path('car_specs/', views.specs, name='Specs'),
    path('buy_form', views.buyform, name='BuyForm'),
    path('buy_success', views.buysuccess, name='BuySuccess'),

    path('rent/', views.rent, name='Rent'),
    path('rent_form/', views.rentform, name='RentForm'),
    path('rent_success/', views.rentsuccess, name='RentSuccess'),

    path('sell_form/', views.sellform, name='SellForm'),
    path('sell_success/', views.rentform, name='SellSuccess'),
    
]


#buy---brand(Unique)---car_specs---buy_form---buy_success