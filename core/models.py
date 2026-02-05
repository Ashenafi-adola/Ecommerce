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
    photo = models.ImageField(upload_to='products/')
    sold_status = models.BooleanField(default=False)
    pre_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='like')
    views = models.ManyToManyField(User, related_name='view')

    def __str__(self):
        return self.description[:50]

class PhoneInfo(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    screen_type = models.CharField(max_length=200)
    screen_resolution = models.CharField(max_length=20)
    ram = models.PositiveIntegerField()
    storage = models.PositiveIntegerField()
    camera = models.PositiveIntegerField()
    battery = models.PositiveIntegerField()

    def __str__(self):
        return self.product


class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name='product')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product, related_name='item')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    