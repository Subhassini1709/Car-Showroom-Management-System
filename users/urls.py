from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='Landing'),
    path('home/',views.home, name='Home Page'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('contact_success/', views.contactsuccess, name='ContactSuccess'),
    
    path('login/', views.loginPage, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='Logout'),

    path('buy/', views.buy, name='Buy'),
    path('buy_dump/',views.buydump, name='BuyDump'),
    path('brand/', views.brand, name='Brand'), 
    path('car_specs/', views.specs, name='Specs'),
    path('buy_form/', views.buyform, name='BuyForm'),
    path('buy_success/', views.buysuccess, name='BuySuccess'),

    path('rent/', views.rent, name='Rent'),
    path('rent_form/', views.rentform, name='RentForm'),
    path('rent_success/', views.rentsuccess, name='RentSuccess'),

    path('sell_form/', views.sellform, name='SellForm'),
    path('sell_success/', views.sellsuccess, name='SellSuccess'),

    path('userrent_form/', views.userrent, name = 'UserRentForm'),
    path('userrent_success/', views.userrentsuccess, name='UserRentSuccess'),

    path('admin_home/', views.adminhome, name='AdminHome'),
    path('admin_add_to_rent/', views.adminaddtorent, name='AdminRent'),
    path('admin_show_rent/', views.adminshowrent, name='ShowRent'),
    path('admin_delete_rent/<int:id>', views.deleterent),
    path('admin_show_rent_requests/', views.adminshowrentrequests, name='ShowRentRequests'),
    path('admin_delete_rent_request/<int:id>', views.deleterentrequest),
    path('admin_show_sell_requests/', views.adminshowsellrequests, name='ShowSellRequests'),
    path('admin_delete_sell_request/<int:id>', views.deletesellrequest),
    path('admin_show_contact_requests/', views.adminshowcontactrequests, name='ShowContactRequests'),
]


#buy---brand(Unique)---car_specs---buy_form---buy_success