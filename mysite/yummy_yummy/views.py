from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

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
    # allproduct = Product.objects.all()
    # allproduct = Product.objects.select_related('Restaurant').all() #join Product and Restaurant table
    query = request.GET.get('q', '')

    if query:
        allproduct = Product.objects.select_related('Restaurant').filter(
            Restaurant=query
        )
    else:
        allproduct = Product.objects.select_related('Restaurant').all()

    product_per_page = 100
    paginator = Paginator(allproduct, product_per_page)
    page = request.GET.get('page')
    allproduct = paginator.get_page(page)

    print("herererr: ",allproduct)
    context = {'allproduct': allproduct}   

    allrow = []
    row = []
    for i,p in enumerate(allproduct):
        if i % 3 ==0:
            if i != 0:
                allrow.append(row)
            row = []
            row.append(p)
        else:
            row.append(p)

    allrow.append(row)
    context['allrow'] = allrow

    context = {
        'allrow': allrow,
        'allproduct': allproduct,
        'title': 'Food Shop Home',
        'shop_name': 'Yummy! Online Menu'
    }

    # Renders the template located at yummy_yummy/templates/yummy_yummy/home.html
    return render(request, 'yummy_yummy/home.html', context)

def fillterSearch(request):
    
    return render(request, 'yummy_yummy/home.html',)

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

def MyRestaurant(request, res_id):
    has_restaurant = Restaurant.objects.filter(User=request.user).exists()
    res = Restaurant.objects.get(User=request.user.id)
    res_name = res.restaurant_name

    myproduct = Product.objects.filter(Restaurant_id=res)

    product_per_page = 3
    paginator = Paginator(myproduct, product_per_page)
    page = request.GET.get('page')
    myproduct = paginator.get_page(page)

    print("herererr: ",myproduct)
    context = {'myproduct': myproduct}

    allrow = []
    row = []
    for i,p in enumerate(myproduct):
        if i % 3 ==0:
            if i != 0:
                allrow.append(row)
            row = []
            row.append(p)
        else:
            row.append(p)

    allrow.append(row)
    context['allrow'] = allrow

    myrestaurnat_id = Restaurant.objects.get(pk=res_id)

    if myrestaurnat_id.User != request.user:
        return HttpResponse("Unauthorized", status=401)

    return render(request, 'yummy_yummy/my_restaurant.html', {
        'has_restaurant': has_restaurant,
        'name': res_name,
        'my_restaurant_id': myrestaurnat_id,
        'myproduct': myproduct,
        'allrow': allrow,
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

def add_product(request, res_id):
    context={}
    myrestaurnat = Restaurant.objects.get(pk=res_id)
    if request.method == 'POST':
        data = request.POST.copy()
        product_title = data.get('title')
        product_price = data.get('price')
        product_description = data.get('description')
        product_available = data.get('product_available')
        
        # validate
        if not product_title or not product_price:
            messages.error(request, "Product name and price are required.")
            return redirect(request.path)

        if product_available == 'yes':
            product_available = True
        else:
            product_available = False
            

        if 'picture' in request.FILES:
            file_image = request.FILES['picture']
            file_image_name = file_image.name.replace(' ', '')
            fs = FileSystemStorage(location='media/product')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(filename)
            print("Picture url:", upload_file_url)
            Product.objects.create(
                Restaurant = myrestaurnat,
                title = product_title,
                picture = 'product' + upload_file_url[6:],
                price = float(product_price),
                description = product_description,
                available = product_available
            )
        messages.success(request, "Add product successfull.")
        return redirect('my-restaurant', res_id=res_id)

    return render(request, 'yummy_yummy/add_product.html', context)

def RestaurantOrder(request):
    return render(request, 'yummy_yummy/restaurant_order.html')