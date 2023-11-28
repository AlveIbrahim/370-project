from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
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
    if request.method=="POST":
        model=request.POST.get("model")
        num_plate=request.POST.get("num_plate")
        num_of_seat=request.POST.get("num_of_seat")
        Drivers_Nid=request.POST.get("Drivers_Nid")
        has_car=request.POST.get("has_car")
        # Driver_driving_license.POST.get("Driver_driving_license")
        car_Listing=car_listing(model=model, num_plate=num_plate, num_of_seat=num_of_seat, Drivers_Nid=Drivers_Nid, has_car=has_car)
        car_Listing.save()
    return render(request, 'car_listing.html')
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

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'Login':login_form})