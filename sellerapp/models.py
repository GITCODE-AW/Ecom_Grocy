from django.db import models
from django.contrib.auth.models import User

class seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars')
    ]

    PAYMENT_CHOICES = [
        ('online', 'Digital Payments'),
        ('offline', 'Cash Payments'),
        ('all', 'Both Digital and Cash Payments')
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    bio = models.CharField(max_length=500, null=True, blank=True, default="")
    payment_option = models.CharField(choices=PAYMENT_CHOICES, max_length=20, default='', null=True, blank=True)
    business_name = models.CharField(max_length=200, default='', null=True, blank=True)
    tax_identification_number = models.CharField(max_length=500, default='', null=True, blank=True)
    business_email = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return self.user.username