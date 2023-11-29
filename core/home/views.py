from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, cl, lst
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
    return redirect('home')

def book(request):
    if request.method == 'POST':
        bk = lst(request.POST, request.FILES)
        if bk.is_valid():
            bk.save()
            return redirect('home_after_login')
    else:
        bk = lst()
    return render(request, 'carinfo.html', {'BK':bk})
