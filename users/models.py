from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class BuyBrand(models.Model):
    BrandID = models.CharField(max_length=100, primary_key=True)
    BrandName = models.CharField(max_length=100)
    NoOfCars = models.IntegerField()

class BuyCar(models.Model):
    BCarID = models.CharField(max_length=100,primary_key=True)
    BCarImage = models.BinaryField()
    BCarName = models.CharField(max_length=100)
    BBrandID = models.ForeignKey(BuyBrand, on_delete=models.CASCADE)
    BNumOfCars = models.IntegerField()

class BuySpecs(models.Model):
    CarID = models.ForeignKey(BuyCar, on_delete=models.CASCADE,primary_key=True)
    Image = models.BinaryField()
    Price = models.FloatField()
    Rating = models.IntegerField()
    Mileage = models.FloatField()
    CC = models.IntegerField()
    SeatingCapacity = models.IntegerField()
    Bootspace = models.IntegerField()
    BodyType = models.CharField(max_length=100)
    FuelType = models.CharField(max_length=100)
    NoOfCylinders = models.IntegerField()
    TransmissionType = models.CharField(max_length=100)
    FuelCapacity = models.FloatField()
    ServiceCost = models.IntegerField()

class BuyBooking(models.Model):
    BCarID = models.ForeignKey(BuyCar, on_delete=models.CASCADE)
    BCustomerID = models.ForeignKey(User,on_delete=models.CASCADE)
    BAddress = models.TextField()
    BPhoneNumber = models.BigIntegerField()

class RentCar(models.Model):
    RCarID = models.CharField(max_length=100,primary_key=True)
    RCarName = models.CharField(max_length=100)
    RImage = models.BinaryField()
    RCarPrice = models.IntegerField()
    RFuel = models.CharField(max_length=100)
    RMileage = models.FloatField()
    RSeatingCapacity = models.IntegerField()

class RentBooking(models.Model): 
    RCustomerID = models.ForeignKey(User,on_delete=models.CASCADE)
    RCarID = models.ForeignKey(RentCar, on_delete=models.CASCADE)
    FromDate = models.DateField()
    ToDate = models.DateField()
    NoOfDays = models.IntegerField()
    RentPerDay = models.ForeignKey(RentCar, on_delete=models.CASCADE)
    TotalRent = models.IntegerField()
    RPhoneNum = models.BigIntegerField()
    RAddress = models.TextField()

class SellCar(models.Model):
    SCustomerID = models.ForeignKey(User,on_delete=models.CASCADE)
    SBrandName = models.CharField(max_length=100)
    SCarName = models.CharField(max_length=100)
    SCarPrice = models.IntegerField()
    KmRun = models.IntegerField()
    CarAge = models.IntegerField()
    SFuel = models.CharField(max_length=100)
    SMileage = models.FloatField()
    SSeatingCapacity = models.IntegerField()




