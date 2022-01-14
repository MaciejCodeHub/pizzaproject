from django.db import models
from django.contrib.auth.models import User


# Creating available menu by staff member
class PizzaType(models.Model):
    name = models.CharField(max_length=255)
    toppings = models.CharField(max_length=255)
    small_price = models.FloatField()
    medium_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return self.name


# Creating an order by customer
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    sauce = models.CharField(max_length=64)
    size = models.CharField(max_length=8)


class OrderInfo(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    card_payment = models.BooleanField()
    remarks = models.CharField(max_length=255)

