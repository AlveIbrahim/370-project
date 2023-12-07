from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing, Customer, Car, Payment, share
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, cl, lst, payment_rent, car_share, ShareSearch
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

@login_required()
def home_after_login(request):
    return render(request,'after_login.html')

@login_required()
def rs(request):
    if request.method == 'POST':
        share_query = ShareSearch(request.POST)
        if share_query.is_valid():
            print(share_query.cleaned_data)
            cars = share.objects.filter(location=share_query.cleaned_data["location"])
            destination = share_query.cleaned_data["destination"]
            return render(request, 'rideshare.html', {
                'share_query':share_query, 
                'cars':cars,
                'destination':destination            
                })
    else:
        share_query = ShareSearch()
    return render(request, 'rideshare.html', {'Share_Search':share_query})

@login_required()
def rent(request):
    return render(request, 'rent.html')
    #return HttpResponse('this is rant page')

@login_required()
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

@login_required()
def logout(request):
    auth_logout(request)
    messages.warning(request, 'You were logged out')
    return redirect('home')

@login_required()
def book(request):
    if request.method == 'POST':
        bk = lst(request.POST, request.FILES)
        if bk.is_valid():
            bk.save()
            return redirect('home_after_login')
    else:
        bk = lst()
    return render(request, 'rentform.html', {'BK':bk})

@login_required()
def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = car_listing.objects.filter(clocation=search_query)
        return render(request, 'search.html', {
            'query':search_query, 
            'posts':posts            
               })
    else:
        return render(request, 'search.html',{})

@login_required()
def payment(request):
    if request.method == 'POST':
        pay = payment_rent(request.POST, request.FILES)
        if pay.is_valid():
            pay.save()
            return redirect('home_after_login')
    else:
        pay = payment_rent()
    return render(request, 'payment.html', {'Payment':pay})

@login_required()
def car_catalog(request):
    car = car_listing.objects.all()
    car_show=list(car)

    return render(request, 'car_catalog.html',{
        'products': car_show
    })

@login_required()
def share_car(request):
    if request.method == 'POST':
        share = car_share(request.POST)
        if share.is_valid():
            share.save()
            return redirect('rs')
    else:
        share = car_share()
    print(request.user.id)
    return render(request, 'share_form.html', {'Car_Share':share})

#cant be bothered to remove below view
@login_required()
def rideshare_search(request):
    context = {'Share_Search':ShareSearch()}
    if request.method == 'POST':
        share_query = ShareSearch(request.POST)
        cars = car_share.objects.filter(location=share_query.cleaned_data["location"])
        destination = share_query.cleaned_data["destination"]
        return render(request, 'rideshare.html', {
            'share_query':share_query, 
            'cars':cars,
            'destination':destination            
               })
    # else:
    #     share_query = ShareSearch()
    return render(request, 'rideshare.html', context=context)