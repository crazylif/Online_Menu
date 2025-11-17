from django.http import HttpResponse
from django.shortcuts import render

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

def login(request):
    return render(request, 'yummy_yummy/login.html')

def register(request):
    return render(request, 'yummy_yummy/register.html')

def profile(request):
    return render(request, 'yummy_yummy/profile.html')