from django import forms
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta():
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2',
        }
    field_order = [
        'username',
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

    class Meta():
        model = UserProfile
        fields = {
            'base_fiat',
            'base_crypto',
            'track_ETH',
            'track_BTC',
            'track_LTC',
            'track_XRP',
            'track_BCH',
            'track_ETC',
            'track_TRX',
            'track_EOS',
            'track_NEO',
            'track_XMR',
            }
        labels = {
            'base_fiat': 'Base Fiat',
            'base_crypto': 'Base Crypto',
            'track_ETH': 'Ethereum',
            'track_BTC': 'Bitcoin',
            'track_LTC': 'Litecoin',
            'track_XRP': 'Ripple',
            'track_BCH': 'Bitcoin Cash',
            'track_ETC': 'Etereum Classic',
            'track_TRX': 'Tronix',
            'track_EOS': 'EOS',
            'track_NEO': 'NEO',
            'track_XMR': 'Monero',
        }
    field_order = [
        'first_name',
        'last_name',    
        'email',  
        'base_fiat',
        'base_crypto',
        'track_ETH',
        'track_BTC',
        'track_LTC',
        'track_XRP',
        'track_BCH',
        'track_ETC',
        'track_TRX',
        'track_EOS',
        'track_NEO',
        'track_XMR',
        ]

    def save(self, commit=True):
        #Create Current Logged In User
        user = super(EditProfileForm, self).save(commit=False)

        #Edit Base User Profile
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        user.save()
        #Create New Data Model
        profile = UserProfile()

        #Fill Data Model With Form and Other Data
        profile.base_user = user
        profile.base_fiat = self.cleaned_data['base_fiat']
        profile.base_crypto = self.cleaned_data['base_crypto']
        profile.cc_ETH = self.cleaned_data['track_ETH'] 
        profile.cc_BTC = self.cleaned_data['track_BTC']
        profile.cc_LTC = self.cleaned_data['track_LTC']
        profile.cc_XRP = self.cleaned_data['track_XRP']
        profile.cc_BCH = self.cleaned_data['track_BCH']
        profile.cc_ETC = self.cleaned_data['track_ETC']
        profile.cc_TRX = self.cleaned_data['track_TRX']
        profile.cc_EOS = self.cleaned_data['track_EOS']
        profile.cc_NEO = self.cleaned_data['track_NEO']
        profile.cc_XMR = self.cleaned_data['track_XMR']

        #Save To DB
        if commit:
            profile.save()
        else:
            print('commit is False')

        return profile

