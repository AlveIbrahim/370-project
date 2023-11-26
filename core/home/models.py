from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    Nid=models.IntegerField(blank = False, null = False, default=0)
    Name=models.CharField(max_length=200)
    Dob=models.DateField(auto_now=False, blank = True, null = True)
    Adress=models.CharField(null=False, max_length=200, default='')
    phn=models.CharField(max_length=11, blank = False, null = False, default='')
    has_car=models.BooleanField(blank=False, null=False, default=False)
    def __str__(self):
        return self.Name

