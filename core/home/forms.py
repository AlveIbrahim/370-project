from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, car_listing, Car


class SignupForm(UserCreationForm):
    # login_id = forms.CharField()
    # password = forms.CharField(max_length=100)
    Customer_Nid = forms.IntegerField()
    Dob = forms.DateField()
    Address = forms.CharField()
    phn = forms.CharField()
    clocation = forms.CharField()
    

    class Meta:
        model = Customer
<<<<<<< HEAD
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'Customer_Nid', 'Dob','Address','phn','clocation')
=======
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'Customer_Nid', 'Dob','Address','phn')
>>>>>>> 2ffdf4b4a804174c8f7e25753a8b170e56055424


class cl(ModelForm):
    
    class Meta:
        model=car_listing
        fields=('model', 
        'num_plate', 
        'num_of_seat', 
        'Drivers_Nid',
        'has_car',
        'Car_image',
<<<<<<< HEAD
        'Driver_driving_license')
=======
        'Driver_driving_license',
        'clocation')
>>>>>>> 2ffdf4b4a804174c8f7e25753a8b170e56055424

class lst(ModelForm):
    
    class Meta:
        model=Car
        fields=('info', 'customer_licence')



<<<<<<< HEAD
=======
class SearchForm(ModelForm):
    class Meta:
        fields = ('location','seatnumber')
  
>>>>>>> 2ffdf4b4a804174c8f7e25753a8b170e56055424
