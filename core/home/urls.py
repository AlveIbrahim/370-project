from django.contrib import admin
from django.urls import path,re_path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('rs', views.rs, name='rs'),
    path('rent', views.rent, name='rent'),
    path('car_Listing', views.car_Listing, name='car_Listing'),
    path('signup', views.signup, name='signup')
]