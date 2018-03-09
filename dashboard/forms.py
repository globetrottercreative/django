from django import forms
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class SearchForm(forms.Form):
    Fiat = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Crypto = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {
            'base_crypto',
            'base_fiat',  
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.base_fiat = self.cleaned_data['base_fiat']
        user.base_crypto = self.cleaned_data['base_crypto']
        user.last_spot = 30

        if commit:
            user.save()

        return user

