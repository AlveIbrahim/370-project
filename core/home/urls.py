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
    path('payment', views.payment, name='payment'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)