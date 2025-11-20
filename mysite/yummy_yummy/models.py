from django.db import models
from django.contrib.auth.models import User

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
