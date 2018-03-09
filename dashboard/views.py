from django.shortcuts import render, redirect
from .forms import SearchForm, RegistrationForm
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
    form = SearchForm()
    user = request.user
    data = {
        'user': user
    }
    return render(request, 'dashboard/home.html', data)

def edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('search/')
    else:
        form = UserChangeForm(instance=request.user)
        args = {
            'form': form,
        }
        return render(request, 'dashboard/edit_profile.html', args)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        args = {
            'form': form,
        }
        return render(request, 'dashboard/register.html', args)