from django import forms
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta():
        model = User
        fields = {
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        }
    field_order = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2']
    def save(self, commit=True):
            #Create Current Logged In User
            user = super(CreateUserForm, self).save(commit=False)

            #Change Native Logged In User Data
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            #Commit to DB
            if commit:
                user.save()

            return user


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    CURRENCY_CHOICES= [
        ('NZD', 'NZD'),
        ('USD', 'USD'),
        ('AUD', 'AUD'),
        ]
    base_fiat = forms.CharField(label='Base Fiat', widget=forms.Select(choices=CURRENCY_CHOICES))
    cc_ETH = forms.BooleanField(label='Ethereum', disabled=True, required=True, initial=True)
    class Meta():
        model = UserProfile
        fields = {
            'base_fiat',
            'cc_ETH',
            'cc_BTC',
            'cc_LTC',
            'cc_XRP',
            'cc_BCH',
            'cc_ETC',
            'cc_TRX',
            'cc_EOS',
            'cc_NEO',
            'cc_XMR',
            }
        labels = {
            'base_fiat': 'Base Fiat',
            'cc_ETH': 'Ethereum',
            'cc_BTC': 'Bitcoin',
            'cc_LTC': 'Litecoin',
            'cc_XRP': 'Ripple',
            'cc_BCH': 'Bitcoin Cash',
            'cc_ETC': 'Etereum Classic',
            'cc_TRX': 'Tronix',
            'cc_EOS': 'EOS',
            'cc_NEO': 'NEO',
            'cc_XMR': 'Monero',
        }
    field_order = [
        'first_name',
        'last_name',    
        'email',  
        'base_fiat',
        'cc_ETH',
        'cc_BTC',
        'cc_LTC',
        'cc_XRP',
        'cc_BCH',
        'cc_ETC',
        'cc_TRX',
        'cc_EOS',
        'cc_NEO',
        'cc_XMR',
        ]

    def save(self, commit=True):
        print('super before')
        #Create Current Logged In User
        user = super(EditProfileForm, self).save(commit=False)
        print('super created')
        #Edit Base User Profile
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        print(user)
        user.save()
        #Create New Data Model
        profile = UserProfile()

        #Fill Data Model With Form and Other Data
        profile.base_user = user
        profile.base_fiat = self.cleaned_data['base_fiat']
        profile.cc_ETH = self.cleaned_data['cc_ETH'] 
        profile.cc_BTC = self.cleaned_data['cc_BTC']
        profile.cc_LTC = self.cleaned_data['cc_LTC']
        profile.cc_XRP = self.cleaned_data['cc_XRP']
        profile.cc_BCH = self.cleaned_data['cc_BCH']
        profile.cc_ETC = self.cleaned_data['cc_ETC']
        profile.cc_TRX = self.cleaned_data['cc_TRX']
        profile.cc_EOS = self.cleaned_data['cc_EOS']
        profile.cc_NEO = self.cleaned_data['cc_NEO']
        profile.cc_XMR = self.cleaned_data['cc_XMR']
        print(profile)
        #Save To DB
        if commit:
            profile.save()
        else:
            print('COMMIT ERROR')

        return profile

