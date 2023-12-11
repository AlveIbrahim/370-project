from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Customer(AbstractUser):
    Customer_Nid=models.IntegerField(blank = False, null = False, default=0)
    Dob=models.DateField(auto_now=False, blank = True, null = True)
    Address=models.CharField(null=False, max_length=200, default='')
    phn=models.CharField(max_length=11, blank = False, null = False, default='')
    
    

class car_listing(models.Model):
    cst = models.ForeignKey(Customer, null= True, on_delete = models.CASCADE)
    model=models.CharField(max_length=200)
    num_plate=models.CharField(max_length=7)
    num_of_seat=models.IntegerField(blank = False, null = False, default=0)
    Drivers_Nid=models.IntegerField(blank = True, null = True, default=0)
    Car_image=models.ImageField(null=True, blank=True)
    Driver_driving_license=models.ImageField(upload_to='image/', null=True, blank=True)
    customer_licence=models.ImageField(upload_to='cimage/', null=True, blank=True)
    clocation=models.CharField(max_length=200, blank = False, null = False, default='')

    PRIVATE = 'Private Car'
    MICRO = 'Micro Bus'
    MINI = 'Mini Bus'
    YES='Yes'
    NO='No'
    TYPE_CHOICES2=[
        (YES, 'Yes'),
        (NO, 'No')
    ]
    TYPE_CHOICES = [
        (PRIVATE, 'Private Car'),
        (MICRO, 'Micro Bus'),
        (MINI, 'Mini Bus'),
    ]
    type_of_car=models.CharField(max_length=200, choices=TYPE_CHOICES, blank = False, null = False, default='')
    has_driver=models.CharField(max_length=7, choices=TYPE_CHOICES2, default='No')    

    
class share(models.Model):
    sharer=models.ForeignKey(Customer, on_delete = models.CASCADE)
    location = models.CharField(null = False, max_length=200)
    destination = models.CharField(null = False, max_length=200)
    type = models.CharField(null=False, max_length=100, default='')
    seats = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(15)])

# class Car(models.Model):
#     customer_licence=models.ImageField(upload_to='cimage/', null=True, blank=True)


class Payment(models.Model):
    tran_number=models.IntegerField(blank = True, null = True, default=0)
    amount=models.IntegerField(blank = True, null = True, default=0)
    inf=models.ForeignKey(Customer, null= True, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=122)
    user_name= models.CharField(blank = True, null = True,max_length=122)
    email = models.CharField(blank = True, null = True,max_length=122)
    phone = models.CharField(blank = True, null = True,max_length=12)
    feedback = models.TextField()
    date = models.DateField()