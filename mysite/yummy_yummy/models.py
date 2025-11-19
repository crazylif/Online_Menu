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
