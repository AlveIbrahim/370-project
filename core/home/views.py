from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, cl
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

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
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        signup = SignupForm()
    return render(request, 'signup.html', {'Signup':signup})