from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # --- Define User Types ---
#     # These choices provide the core definition for each role
#     class Types(models.TextChoices):
#         CUSTOMER = "CUSTOMER", "Customer"
#         SELLER = "SELLER", "Seller"
#         ADMIN = "ADMIN", "Admin"

#     # --- User Type Field ---
#     user_type = models.CharField(
#         max_length=50,
#         choices=Types.choices,
#         default=Types.CUSTOMER,
#         verbose_name="User Role"
#     )

#     # --- Other necessary shop fields ---
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.TextField(blank=True)

#     def is_customer(self):
#         return self.user_type == self.Types.CUSTOMER

#     def is_seller(self):
#         return self.user_type == self.Types.SELLER
    
#     def is_admin(self):
#         return self.user_type == self.Types.ADMIN
    
    
# class CustomerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # Add fields specific to a customer
#     favorite_shops = models.ManyToManyField('Shop', blank=True) # Assuming you have a Shop model
#     loyalty_points = models.IntegerField(default=0)
    
#     def __str__(self):
#         return f"Customer Profile for {self.user.username}"


# class SellerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     shop_name = models.CharField(max_length=100, unique=True)
#     shop_description = models.TextField(blank=True)
#     is_approved = models.BooleanField(default=False) # Important for moderation/onboarding
    
#     def __str__(self):
#         return f"Seller Profile: {self.shop_name}"