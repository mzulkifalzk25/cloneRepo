from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='media')
    category = models.CharField(max_length=100, default="")
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    @classmethod
    def add_to_cart(cls, user, product):
        cart, created = cls.objects.get_or_create(user=user, product=product)
        return cart
