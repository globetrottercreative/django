from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Portfolio(models.Model):
    ETH_Portfolio = models.IntegerField(default=0)
    BTC_Portfolio = models.IntegerField(default=0)
    LTC_Portfolio = models.IntegerField(default=0)
    XRP_Portfolio = models.IntegerField(default=0)
    BCH_Portfolio = models.IntegerField(default=0)
    ETC_Portfolio = models.IntegerField(default=0)
    TRX_Portfolio = models.IntegerField(default=0)
    EOS_Portfolio = models.IntegerField(default=0)
    NEO_Portfolio = models.IntegerField(default=0)
    XMR_Portfolio = models.IntegerField(default=0)

class UserProfile(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    wallet = models.OneToOneField(Portfolio, on_delete=models.CASCADE, default=' ')
    base_fiat = models.CharField(max_length=3, default='NZD')
    last_spot = models.FloatField(default=1.00)
    cc_ETH = models.BooleanField(default=True)
    cc_BTC = models.BooleanField(default=False)
    cc_LTC = models.BooleanField(default=False)
    cc_XRP = models.BooleanField(default=False)
    cc_BCH = models.BooleanField(default=False)
    cc_ETC = models.BooleanField(default=False)
    cc_TRX = models.BooleanField(default=False)
    cc_EOS = models.BooleanField(default=False)
    cc_NEO = models.BooleanField(default=False)
    cc_XMR = models.BooleanField(default=False)

    def __str__(self):
        return self.base_user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(base_user=kwargs['instance'])

post_save.connect(create_profile, sender=User) # link the trigger(signal). When User model is saved, call create_profile.