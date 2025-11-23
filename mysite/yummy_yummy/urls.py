from django.urls import path

# from .views import home,home2,aboutUs
from .views import *
# from django.contrib.auth import views
from . import views

urlpatterns = [
  path('', home, name='home'),
  path('home2/', home2, name="home2"),
  path('base/', base, name="base"),
  path('login/', login_user, name="login"),
  path('logout/', logout_user, name="logout"),
  path('register/', register, name="register"),
  path('profile/', profile, name="profile"),
  path('myrestaurant/<int:res_id>/', MyRestaurant, name="my-restaurant" ),
  path('registerMyrestaurant/', register_MyRestaurant, name="register-myrestaurant"),
  path('myrestaurant/<int:res_id>/addproduct/', add_product, name='add-product'),
  path('delete/<int:product_id>', delete_product, name='delete-product'),
  path('add-to-cart/<int:product_id>', add_to_cart, name='add_to_cart' ),
  path('add_quantity/<int:cart_id>', add_quantity, name='add_quantity' ),
  path('minus_quantity/<int:cart_id>', minus_quantity, name='minus_quantity' ),
  path('delete_cart_item/<int:cart_id>', delete_cart_item, name='delete_cart_item' ),
  path('cart/', cart_page, name='cart_page'),
  path('pay/', payout, name="pay_cart"),
  path('my-order/', myOrder, name="my_order"),
  path('myrestaurant/<int:res_id>/order/', RestaurantOrder, name="restaurant_order"),
  path('cook_order/<int:order_id>', Cook_order, name="cook_order"),
  path('done_order/<int:order_id>', Done_order, name="done_order"),
  path('cancel_order/<int:order_id>', Cancel_order, name="cancel_order"),

]