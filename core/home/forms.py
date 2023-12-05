from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, car_listing, Car, Payment


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
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'Customer_Nid', 'Dob','Address','phn')


class cl(ModelForm):
    
    class Meta:
        model=car_listing
        fields=('model', 
        'num_plate', 
        'num_of_seat', 
        'Drivers_Nid',
        'has_car',
        'Car_image',
        'Driver_driving_license',
        'clocation')

class lst(ModelForm):
    
    class Meta:
        model=Car
        fields=('info', 'customer_licence')



class SearchForm(ModelForm):
    class Meta:
        fields = ('location','seatnumber')

class payment_rent(ModelForm):
    
    class Meta:
        model=Payment
        fields=('tran_number', 'amount')
  
