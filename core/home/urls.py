from django.contrib import admin
from django.urls import path,re_path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('home_after_login',views.home_after_login,name='home_after_login'),
    path('rs', views.rs, name='rs'),
    path('rent', views.rent, name='rent'),
    path('car_Listing', views.car_Listing, name='car_Listing'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('book', views.book, name='book'),
    path('search', views.search_feature, name='search'),
    path('payment/<str:plate>', views.payment, name='payment'),
    path('car_catalog', views.car_catalog, name='car_catalog'),
    path('share_form', views.share_car, name='share_form'),
    path('share_search', views.rideshare_search, name='share_search'),
    path('car_micro', views.car_micro, name='car_micro'),
    path('car_private', views.car_private, name='car_private'),
    path('car_mini', views.car_mini, name='car_mini'),
    path('contact', views.contact, name='contact'),
    # path('multiply_private', views.multiply_private, name='multiply_private'),
    # path('multiply_micro', views.multiply_micro, name='multiply_micro'),
    # path('multiply_mini_bus', views.multiply_mini_bus, name='multiply_mini_bus'),
    path('ren_amount_private/<str:plate>', views.ren_amount_private, name='ren_amount_private'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)