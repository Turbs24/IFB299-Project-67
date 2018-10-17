"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.generic.base import TemplateView
from crcapp import views
from accounts import views as accountview

urlpatterns = [
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
	path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
	path('admin/', admin.site.urls),
	re_path(r'^cars/(\d+)/', views.car_details, name= 'car_details'),
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', accountview.SignUp.as_view(), name='signup'),
	path('deals/', TemplateView.as_view(template_name='deals.html'), name='deals'),
	path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
	path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
	path('booking/', TemplateView.as_view(template_name='booking.html'), name='bookings'),
	re_path(r'^vehicles$',views.vehicles, name ='vehicles'),
	re_path(r'^locations$',views.locations, name ='locations'),

]
