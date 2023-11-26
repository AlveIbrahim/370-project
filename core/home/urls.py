from django.contrib import admin
from django.urls import path,re_path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('rs', views.rs, name='rs'),
    path('rant', views.rant, name='rant'),
    path('contact', views.contact, name='contact'),
]