from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    Customer_Nid=models.IntegerField(blank = False, null = False, default=0)
    Dob=models.DateField(auto_now=False, blank = True, null = True)
    Address=models.CharField(null=False, max_length=200, default='')
    phn=models.CharField(max_length=11, blank = False, null = False, default='')
    
    

class car_listing(models.Model):
    model=models.CharField(max_length=200)
    num_plate=models.CharField(max_length=7)
    num_of_seat=models.IntegerField(blank = False, null = False, default=0)
    Drivers_Nid=models.IntegerField(blank = True, null = True, default=0)
    has_car=models.CharField(max_length=7, default='No')
    Car_image=models.ImageField(null=True, blank=True)
    Driver_driving_license=models.ImageField(upload_to='image/', null=True, blank=True)
    clocation=models.CharField(max_length=200, blank = False, null = False, default='')
    
    

class Car(models.Model):
    info=models.ForeignKey(car_listing, on_delete = models.CASCADE)
    customer_licence=models.ImageField(upload_to='cimage/', null=True, blank=True)