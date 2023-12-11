from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing, Customer, Payment, share, Contact, Notification
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, cl, payment_rent, car_share, ShareSearch
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from datetime import datetime
from django.contrib import admin
from django.urls import path

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

@login_required()
def home_after_login(request):
    car = car_listing.objects.all()                                                  

    car_list = list(car)

    # Randomly suffling      
    random.shuffle(car_list)  
    lst=[]
    for i in range(0,3):
        lst.append(car_list[i])
    return render(
        request, 'after_login.html',
        {
            'Cars': lst,
            'request': request,            
        })


@login_required()
def rs(request):
    if request.method == 'POST':
        share_query = ShareSearch(request.POST)
        sharing_customer = request.POST.get('sharer')
        current_user = request.user
        pickup = request.POST.get('location')
        drop = request.POST.get('destination')
        if sharing_customer!=None:
            sharer = Customer.objects.get(username=sharing_customer)
            notif_text = f'{current_user} would like to share your ride (Location={pickup}, Destination={drop})'
            notif = Notification(sender=current_user, reciever=sharer, message=notif_text, notif_type='share_req')
            notif.save()
        if share_query.is_valid():
            cars = share.objects.filter(location=share_query.cleaned_data["location"])
            destination = share_query.cleaned_data["destination"]
            return render(request, 'rideshare.html', {
                'Share_Search':ShareSearch(),
                'share_query':share_query, 
                'cars':cars,
                'destination':destination,
                'current_user':current_user
                })
        else:
            print(share_query.errors.as_data())
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
        # form=request.POST
        # if form.get('customer_licence'):
        #     customer_licence = request.POST.get('customer_licence')
        #     customer_licence.save()
        c_l = cl(request.POST, request.FILES)
        if c_l.is_valid():
            listing = c_l.save(commit=False)
            listing.cst = request.user
            listing.save()
            return redirect('home_after_login')
        else:
            print(c_l.errors.as_data())
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
            print(signup.errors.as_data())
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
            print(login_form.errors.as_data())
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
def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = car_listing.objects.filter(clocation=search_query.lower())
        return render(request, 'search.html', {
            'query':search_query, 
            'posts':posts            
               })
    else:
        return render(request, 'search.html',{})

@login_required()
def payment(request,plate):
    car = car_listing.objects.get(num_plate=plate)
    day=request.GET['days']
    owner=request.user
    if car.has_driver=="No":
        if car.type_of_car=="Private Car":
            amoun=int(day)*8500
        elif car.type_of_car=="Micro Bus":
            amoun=int(day)*11500
        elif car.type_of_car=="Mini Bus":
            amoun=int(day)*18500
    elif car.has_driver=="Yes":
        if car.type_of_car=="Private Car":
            amoun=int(day)*10000
        elif car.type_of_car=="Micro Bus":
            amoun=int(day)*13000
        elif car.type_of_car=="Mini Bus":
            amoun=int(day)*20000         
    if request.method == 'POST':
        pay = payment_rent(request.POST, request.FILES)
        if pay.is_valid():
            pay.save()
            return redirect('home_after_login')
        else:
            print(pay.errors.as_data())
    else:
        pay = payment_rent()
    return render(request, 'payment.html',{
            'Payment':pay,
        'amoun':amoun, 'owner':owner})
  

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
            complete_share = share.save(commit=False)
            complete_share.sharer = request.user
            complete_share.save()
            return redirect('rs')
        else:
            print(share.errors.as_data())
    else:
        share = car_share()
    print(request.user)
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


def car_micro(request):
    car1 = car_listing.objects.filter(type_of_car="Micro Bus")
    car_show1=list(car1)
    abc = request.user
    return render(request, 'car_micro.html',{
        'products': car_show1,
        'user': abc
    })

def car_private(request):
    car1 = car_listing.objects.filter(type_of_car="Private Car")
    car_show1=list(car1)
    abc = request.user
    return render(request, 'car_micro.html',{
        'products': car_show1,
        'user': abc
    })

def car_mini(request):
    car1 = car_listing.objects.filter(type_of_car="Mini Bus")
    car_show1=list(car1)
    abc = request.user
    return render(request, 'car_micro.html',{
        'products': car_show1,
        'user': abc
    })
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user_name=request.POST.get('user_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')
        cont = Contact(name=name, user_name=user_name, email=email, phone=phone,feedback=feedback, date = datetime.today())
        cont.save()
        return redirect('home_after_login')
    return render(request, 'contact.html')

# def multiply_private(request):
#     day=request.GET['days']
#     amoun=int(day)*10000
#     return render(request, 'show_amount.html', {'amoun':amoun})

# def multiply_micro(request):
#     day=request.GET['days']
#     amoun=int(day)*13000
#     return render(request, 'show_amount.html', {'amoun':amoun})

# def multiply_mini_bus(request):
#     day=request.GET['days']
#     amoun=int(day)*20000
#     return render(request, 'show_amount.html', {'amoun':amoun})

def ren_amount_private(request,plate):

    return render(request, 'ren_amount_private.html',{'plate':plate})

def context_processor(request):
    if request.user.is_authenticated:
        notification = Notification.objects.filter(reciever=request.user)
        notif_num = len(notification)
        return {'notification': notification, 'notif_num': notif_num}
    else:
        return {'notification': None, 'notif_num': None}

@login_required
def notification_view(request):
    if request.method=='POST':
        notif_id = request.POST.get("notif_id")
        selected_notif = Notification.objects.get(id=notif_id)
        if 'delete' in request.POST:
            selected_notif.delete()
        elif 'accept' in request.POST:
            phone_num =  request.user.phn
            print(phone_num)
            notif = Notification(sender=request.user, reciever=selected_notif.sender, message=f'Your request has been accepted, please contact the ride sharer. Phone: {phone_num}', notif_type='accepted')
            notif.save()
    return render(request, 'notification.html')