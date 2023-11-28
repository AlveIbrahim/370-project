from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, cl
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

def home_after_login(request):
    return render(request,'after_login.html')

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
            return redirect('home_after_login')
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
            auth_login(request, user)
            return redirect('home_after_login')
        else:
            return redirect('signup')
    else:
        signup = SignupForm()
    return render(request, 'signup.html', {'Signup':signup})

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request,user)
            return redirect('home_after_login')
        else:
            return redirect('login')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'Login':login_form})

def logout(request):
    auth_logout(request)
    messages.warning(request, 'You were logged out')
<<<<<<< HEAD
    return redirect('home')
=======
    return redirect('home')
>>>>>>> fa0b78e28eb1464b8d1813024a8d3b7482331371
