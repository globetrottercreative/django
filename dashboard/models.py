from django.db import models

# Create your models here.
class UserProfile(models.Model):
    base_fiat = models.CharField(max_length=3, default='')
    base_crypto = models.CharField(max_length=3, default='')
    last_spot = models.FloatField(default=0.00)
