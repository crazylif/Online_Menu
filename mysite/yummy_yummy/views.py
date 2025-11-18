from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# In a Django view:
def dashboard_view(request):
    if request.user.is_seller():
        return render(request, 'seller_dashboard.html')
    elif request.user.is_admin():
        return render(request, 'admin_panel.html')
    else: # Default to customer
        return render(request, 'customer_home.html')

# Create your views here.
def home(request):
    # Data to pass to the template
    context = {
        'title': 'Food Shop Home',
        'shop_name': 'Yummy Yummy Online Menu'
    }

    # Renders the template located at yummy_yummy/templates/yummy_yummy/home.html
    return render(request, 'yummy_yummy/home.html', context)

def home2(request):
  return HttpResponse('<h1 style="color:red; font-size: 300%;">Hello World</h1>')

def base(request):
    return render(request, 'yummy_yummy/base.html')

def login_user(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            context['message'] = "You have been logged in."
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again!")
            context['message'] = "username or password is incorrect."
            return redirect('login')  
    else:
        return render(request, 'yummy_yummy/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')

def register(request):
    context={}
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirmpassword = data.get('confirmpassword')

        try:
            User.objects.get(username=username)
            context['message'] = "Username duplicate"
        except:
            newuser = User()
            newuser.username = username
            newuser.email = email

            if (password == confirmpassword):
                newuser.set_password(password)
                newuser.save()
                newprofile = Profile()
                newprofile.user = User.objects.get(username=username)
                newprofile.save()
                context['message'] = "register completed."
                messages.success(request, ("register completed."))
                return redirect('login')
            else:
                context['message'] = "password and confirm password in incorrect."
    return render(request, 'yummy_yummy/register.html', context)

def profile(request):
    return render(request, 'yummy_yummy/profile.html')

def MyRestaurant(request):
    return render(request, 'yummy_yummy/my_restaurant.html')

def RestaurantOrder(request):
    return render(request, 'yummy_yummy/restaurant_order.html')