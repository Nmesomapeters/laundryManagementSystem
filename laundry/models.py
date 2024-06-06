from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    num_shirts = models.IntegerField(default=0)
    num_pants = models.IntegerField(default=0)
    num_suits = models.IntegerField(default=0)
    num_skirts = models.IntegerField(default=0)
    num_dresses = models.IntegerField(default=0)
    num_others = models.IntegerField(default=0)
    special_requests = models.TextField(blank=True, null=True)
    pickup_date = models.DateField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_verified = models.BooleanField(default=False)
    
    def total_clothes(self):
        return (self.num_shirts + self.num_pants + self.num_suits + 
                self.num_skirts + self.num_dresses + self.num_others)
    
    def calculate_total_amount(self):
        total_amount = 0
        service_carts = self.servicecart_set.all()
        for service_cart in service_carts:
            total_amount += service_cart.service.price
        
        self.total_amount = total_amount
        self.save()  # Save the total_amount to the database
        return total_amount

class ServiceCart(models.Model):
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        service = models.ForeignKey(Service, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
              return self.service.name
        

class Checkout(models.Model):
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        full_name = models.CharField(max_length=100)
        email_id = models.EmailField(max_length=100)
        delivery_address = models.CharField(max_length=255)
        phone_number = models.CharField(max_length=20)
        payment_method = models.CharField(max_length=20) 
        timestamp = models.DateTimeField(auto_now_add=True)
       


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.name
