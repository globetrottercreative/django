from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm, CreateUserForm
from dashboard.models import UserProfile
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
    user = request.user
    data = {
        'user': user
    }
    return render(request, 'dashboard/home.html', data)

def newuser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateUserForm()
        args = {
            'form': form,
        }
        return render(request, 'dashboard/newuser.html', args)

def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    else:
        profile = UserProfile.objects.get(base_user=request.user)
        form = EditProfileForm(initial={
            'base_crypto': profile.base_crypto,
            'base_fiat': profile.base_fiat,
            })
        args = {
            'form': form,
            'user': profile
        }
        return render(request, 'dashboard/editprofile.html', args)