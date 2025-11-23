from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  usertype = models.CharField(max_length=100, default='user')

  def __str__(self):
    return self.user.username
  
class Restaurant(models.Model):
  Restaurant_ID = models.AutoField(primary_key=True)
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  restaurant_name = models.CharField(max_length=255)

  def __str__(self):
    return self.restaurant_name
  
class Product(models.Model):
  Product_ID = models.AutoField(primary_key=True)
  Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
  title = models.CharField(max_length=100)
  picture = models.ImageField(upload_to='product')
  description = models.CharField(max_length=255)
  price = models.FloatField()
  available = models.BooleanField(default=True)

  def __str__(self):
    return self.title
  
class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  product = models.ForeignKey(Product , on_delete=models.CASCADE)
  product_name = models.CharField(max_length=100, default="")
  quantity = models.IntegerField(default=1)

  def subtotal(self):
    return self.product.price * self.quantity
  
class Order(models.Model):
  Order = models.AutoField(primary_key=True)
  Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  picture = models.ImageField(upload_to='product')
  restaurant_name = models.CharField(max_length=255)
  user_name = models.CharField(max_length=100)
  price = models.FloatField(default=0)
  quatity = models.IntegerField()
  total_price = models.FloatField()
  status =models.CharField(default='Wait')
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title
  
class Order_history(models.Model):
  Order = models.AutoField(primary_key=True)
  Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  User = models.ForeignKey(User, on_delete=models.CASCADE)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  picture = models.ImageField(upload_to='product')
  restaurant_name = models.CharField(max_length=255)
  user_name = models.CharField(max_length=100)
  price = models.FloatField(default=0)
  quatity = models.IntegerField()
  total_price = models.FloatField()
  status =models.CharField(default='Wait')
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title
