from django.shortcuts import render, redirect, HttpResponse
from home.models import car_listing, Customer, Payment, share, Contact, Notification, cs_driver_ifo
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
from django.utils import timezone

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
    j=0
    for i in range(len(car_list)):
        if j==3:
            break
        else:
            lst.append(car_list[i])
            j+=1

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
        seat_num = request.POST.get('seats')
        if sharing_customer!=None:
            sharer = Customer.objects.get(username=sharing_customer)
            notif_text = f'{current_user} would like to share your ride (Location={pickup}, Destination={drop})'
            notif = Notification(sender=current_user, reciever=sharer, message=notif_text, notif_type='share_req', car=seat_num)
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
        posts = car_listing.objects.filter(clocation__contains=search_query.lower())
        print(search_query)
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
            amoun=int(day)*11000
        elif car.type_of_car=="Mini Bus":
            amoun=int(day)*17500
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
            pay.inf=owner
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
    abc = request.user
    if request.method=="POST":
        cr=request.POST.get('adad')
        kl=car_listing.objects.get(id=cr)
        if 'ondelete' in request.POST:
            kl.delete()
        return render(request, 'car_catalog.html',{
            'products': car_show,
            'user': abc
    })
    print(abc)
    return render(request, 'car_catalog.html',{
        'products': car_show,
        'user': abc
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
    if request.method == 'POST':
        customer_licence=request.POST.get('customer_licence')
        tk=cs_driver_ifo(customer_licence=customer_licence, cst2=abc)
        tk.save()
    return render(request, 'car_micro.html',{
        'products': car_show1,
        'user': abc
    })

def car_private(request):
    car1 = car_listing.objects.filter(type_of_car="Private Car")
    car_show1=list(car1)
    abc = request.user
    if request.method == 'POST':
        customer_licence=request.POST.get('customer_licence')
        tk=cs_driver_ifo(customer_licence=customer_licence, cst2=abc)
        tk.save()

    return render(request, 'car_micro.html',{
        'products': car_show1,
        'user': abc
    })

def car_mini(request):
    car1 = car_listing.objects.filter(type_of_car="Mini Bus")
    car_show1=list(car1)
    abc = request.user
    if request.method == 'POST':
        customer_licence=request.POST.get('customer_licence')
        tk=cs_driver_ifo(customer_licence=customer_licence, cst2=abc)
        tk.save()
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
        elif 'decline' in request.POST:
            notif = Notification(sender=request.user, reciever=selected_notif.sender, message=f'Your request has been declined.', notif_type='declined')
            notif.save()
            selected_notif.delete()
        elif 'accept' in request.POST:
            phone_num =  request.user.phn
            notif = Notification(sender=request.user, reciever=selected_notif.sender, message=f'Your request has been accepted, please contact the ride sharer. Phone: {phone_num}', notif_type='accepted')
            notif.save()
            selected_notif.delete()
    return render(request, 'notification.html')

def start_share(request):
    hidden = Notification.objects.filter(notif_type='hidden')
    count = len(hidden)
    print(count)
    if request.method=='POST':
        if count==1:
            hidden_object = Notification.objects.get(notif_type='hidden')
            start_time = hidden_object.timestamp
            total_time = timezone.now() - start_time
            hidden_object.delete()
            return render(request, 'start_share.html', {'amount':(total_time.total_seconds())*0.3})
        if count==0:
            hidden_notif = Notification(sender=request.user, reciever=request.user, notif_type='hidden')
            hidden_notif.save()
            return render(request, 'start_share.html', {'stop': 'stop'})
        else:
            hidden_notif = Notification(sender=request.user, reciever=request.user, notif_type='hidden')
            hidden_notif.save()
            return render(request, 'start_share.html', {'stop': 'stop'})
    
    else:
        if count==1:
            return render(request, 'start_share.html', {'stop': 'stop'})
        return render(request, 'start_share.html')