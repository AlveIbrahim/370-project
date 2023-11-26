from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

def rs(request):
    return HttpResponse('this is Ride Sharing page')

def rant(request):
    return HttpResponse('this is rant page')

def contact(request):
    return HttpResponse('this is contact page')