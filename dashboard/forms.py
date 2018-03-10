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
            }
        labels = {
            'base_fiat': 'Base Fiat',
            'base_crypto': 'Base Crypto',
        }
    field_order = [
        'first_name',
        'last_name',    
        'email',  
        'base_fiat',
        'base_crypto',
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

        #Save To DB
        if commit:
            profile.save()
        else:
            print('commit is False')

        return profile

