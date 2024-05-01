from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

class Bike(models.Model):
    bike_name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE,null=True)
    booking_date = models.DateField()
    return_date = models.DateField()
    start_time = models.TimeField(default=str(datetime.now().time()))
    end_time = models.TimeField(default=str(datetime.now().time()))
    status = models.CharField(max_length=50, default='Pending')
    booking_created_at = models.DateTimeField(auto_now_add=True)
    admin_id = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.customer.user.username} - {self.bike.bike_name}'

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)


class Invoice(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
