from django.db import models
from sellerapp.models import seller

class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category

class Subcategory(models.Model):
    subcategory = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.subcategory

class Product(models.Model):
    seller = models.ForeignKey(seller, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    brand_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True, blank=True)
    Subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=20)
    image = models.ImageField(upload_to='productapp\product_images', null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.product_name