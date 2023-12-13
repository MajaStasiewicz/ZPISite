from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default="black")
    price = models.DecimalField(
        decimal_places = 2,
        max_digits = 8,
        validators = [MinValueValidator(0)]
    )

    def __str__(self):
        return self.name
    
class UserItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=1)
    hand = models.CharField(max_length=50, default="PRAWORECZNOSC")
    size = models.CharField(max_length=20, default="180x60")
    drawer = models.CharField(max_length=20, default="BEZ SZUFLADY")
    shredder = models.CharField(max_length=20, default="BEZ NISZCZARKI")
    water = models.CharField(max_length=20, default="BEZ DOZOWNIKA")
    price = models.DecimalField(
        decimal_places = 2,
        max_digits = 8,
        validators = [MinValueValidator(0)],
    )
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telephone = models.PositiveIntegerField(default=1)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    delivery_method = models.CharField(max_length=10)

    def __str__(self):
        return self.name