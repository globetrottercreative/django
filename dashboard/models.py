from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    base_fiat = models.CharField(max_length=3, default='')
    base_crypto = models.CharField(max_length=3, default='')
    last_spot = models.FloatField(default=0.00)
