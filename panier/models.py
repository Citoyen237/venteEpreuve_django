from django.db import models
from auth_app.models import CustomUser as User
from abonnement.models import Pack as Product
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def expiration_date(self):
        return self.order.created_at + relativedelta(months=self.product.duree)
   

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        return total
    def __str__(self):
        return f"Cart of {self.user.first_name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

   
    def get_total_price(self):
        return self.product.prix * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"
    