from django import forms
from dashboard.models import UserProfile

class SearchForm(forms.Form):
    Fiat = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Crypto = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class RegistrationForm(forms.Form):
    user = UserProfile.user
    class Meta:
        model = UserProfile
        fields = (
            'user', 
            'base_fiat',
            'base_crypto',
            'last_spot'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.base_fiat = self.cleaned_data['email']
        user.base_crypto = self.cleaned_data['email']

        if commit:
            user.save()

        return user

