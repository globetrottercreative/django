from django.shortcuts import render, redirect
from .forms import SearchForm, RegistrationForm
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def catcher(request):
    form = SearchForm()
    user = request.user
    print(user)
    data = {
        'name': 'I\'m The Name',
        'form': form,
        'id_name': user
    }
    return render(request, 'dashboard/search.html', data)

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
            return redirect('home/')
    else:
        form = RegistrationForm()
        args = {
            'form': form,
        }
        return render(request, 'dashboard/register.html', args)