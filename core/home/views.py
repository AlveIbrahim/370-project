from django.shortcuts import render, HttpResponse
from home.models import car_listing

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