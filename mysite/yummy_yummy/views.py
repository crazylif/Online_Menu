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
        'shop_name': 'Yummy! Online Menu'
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
    has_restaurant = Restaurant.objects.filter(User=request.user).exists()
    res_name = Restaurant.objects.get(User=request.user.id)
    res_name = res_name.restaurant_name

    return render(request, 'yummy_yummy/my_restaurant.html', {
        'has_restaurant': has_restaurant,
        'name': res_name
    })

def register_MyRestaurant(request):
    context={}
    if request.method == 'POST':
        data = request.POST.copy()
        restaurant_name = data.get('restaurant_name')
        
        
        if Restaurant.objects.filter(restaurant_name=restaurant_name).exists():
            context['message'] = "Restaurant name is duplicated."
            messages.success(request, ("Restaurant name is duplicated."))
            return render(request, 'yummy_yummy/register_Myrestaurant.html', context)
    
        # Create restaurant linked to the logged-in user
        Restaurant.objects.create(
            User_id=request.user.id,
            restaurant_name=restaurant_name
        )
        # Update profile usertype
        profile = Profile.objects.get(user=request.user)
        profile.usertype = "seller"
        profile.save()

        messages.success(request, ("regiter restaurant completed."))
        return redirect('my-restaurant')

    return render(request, 'yummy_yummy/register_Myrestaurant.html', context)

def add_product(request):
    return render(request, 'yummy_yummy/add_product.html')

def RestaurantOrder(request):
    return render(request, 'yummy_yummy/restaurant_order.html')