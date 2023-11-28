from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing
from django.contrib.auth.forms import AuthenticationForm
<<<<<<< HEAD
from django.contrib import messages
from .forms import SignupForm, cl
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
=======
from .forms import SignupForm, cl
from django.contrib.auth import login
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

<<<<<<< HEAD
def home_after_login(request):
    return render(request,'after_login.html')

=======
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa
def rs(request):
    return render(request, 'rideshare.html')
    #return HttpResponse('this is Ride Sharing page')

def rent(request):
    return render(request, 'rent.html')
    #return HttpResponse('this is rant page')

def car_Listing(request):
    if request.method == 'POST':
        c_l = cl(request.POST, request.FILES)
        if c_l.is_valid():
            c_l.save()
            return redirect('home')
    else:
        c_l = cl()
    return render(request, 'car_listing.html', {'CL':c_l})
    # if request.method=="POST":
    #     model=request.POST.get("model")
    #     num_plate=request.POST.get("num_plate")
    #     num_of_seat=request.POST.get("num_of_seat")
    #     Drivers_Nid=request.POST.get("Drivers_Nid")
    #     has_car=request.POST.get("has_car")
    #     Car_image=request.POST.get("Car_image")
    #     # Driver_driving_license.POST.get("Driver_driving_license")
    #     car_Listing=car_listing(model=model, num_plate=num_plate, num_of_seat=num_of_seat, Drivers_Nid=Drivers_Nid, has_car=has_car, Car_image=Car_image)
    #     car_Listing.save()
    # return render(request, 'car_listing.html')
    #return HttpResponse('this is contact page')

def signup(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            user = signup.save()
<<<<<<< HEAD
            auth_login(request, user)
            return redirect('home_after_login')
=======
            login(request, user)
            return redirect('home')
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa
        else:
            return redirect('signup')
    else:
        signup = SignupForm()
    return render(request, 'signup.html', {'Signup':signup})

<<<<<<< HEAD
def login(request):
=======
def login_view(request):
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
<<<<<<< HEAD
            auth_login(request,user)
            return redirect('home_after_login')
=======
            login(request,user)
            return redirect('home')
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa
        else:
            return redirect('login')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'Login':login_form})
<<<<<<< HEAD

def logout(request):
    auth_logout(request)
    messages.warning(request, 'You were logged out')
    return redirect('home')
=======
>>>>>>> 38c90125a8f265e08c0bc94a3a4b2b051824acaa
