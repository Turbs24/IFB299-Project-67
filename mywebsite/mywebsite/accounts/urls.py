# accounts/urls.py

from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.SignUp.as_view(), name='signup'),
]