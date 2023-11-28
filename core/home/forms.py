from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class SignupForm(UserCreationForm):
    #login_id = forms.CharField()
    #password = forms.CharField(max_length=100)
    Customer_Nid = forms.IntegerField()
    Dob = forms.DateField()
    Address = forms.CharField()
    phn = forms.CharField()
    

    class Meta:
        model = Customer
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'Customer_Nid', 'Dob','Address','phn')