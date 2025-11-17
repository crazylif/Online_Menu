from django.urls import path

# from .views import home,home2,aboutUs
from .views import *
# from django.contrib.auth import views
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home2', home2, name="home2"),
  path('base', base, name="base"),
  path('login', login, name="login"),
  path('register', register, name="register"),
  path('profile', profile, name="profile"),
]