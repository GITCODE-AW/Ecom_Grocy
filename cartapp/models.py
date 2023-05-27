from django.db import models
from django.contrib.auth.models import User
import productapp.models as productapp_models
import sellerapp.models as sellerapp_models


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.user.username


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(productapp_models.Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.product.product_name


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(sellerapp_models.seller, on_delete=models.CASCADE)
    product = models.ForeignKey(productapp_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    # future feature
    varient = models.CharField(max_length=300, default='', null=True, blank=True)
    price = models.PositiveIntegerField(default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"buyer {self.buyer.username},seller {self.seller.user.username}"