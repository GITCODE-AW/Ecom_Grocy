from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
    state = models.CharField(max_length=40, blank=True, null=True, default=None)
    city = models.CharField(max_length=40, blank=True, null=True, default=None)
    address = models.TextField(blank=True, null=True, default=None)
    phone = models.IntegerField(blank=True, null=True, default=None)
    email_token = models.CharField(max_length=200, null=True, blank=True, default='')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# raw temperary table for email verfication and setting passwords
class Verification(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=400)
    is_verified = models.BooleanField(default=False)