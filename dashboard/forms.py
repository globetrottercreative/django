from django import forms

class SearchForm(forms.Form):
    Fiat = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Crypto = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

