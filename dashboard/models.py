from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE)
    base_fiat = models.CharField(max_length=3, default='')
    base_crypto = models.CharField(max_length=3, default='')
    last_spot = models.FloatField(default=1.00)
    def __str__(self):
        return self.title

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(base_user=kwargs['instance'])

post_save.connect(create_profile, sender=User) # link the trigger(signal). When User model is saved, call create_profile.