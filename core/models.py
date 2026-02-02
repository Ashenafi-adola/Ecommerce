from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    photo = models.ImageField()
    sold_status = models.BooleanField(default=False)
    cart_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Cart(models.Model):
    producs = models.ManyToManyField(Product, related_name='product')
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    