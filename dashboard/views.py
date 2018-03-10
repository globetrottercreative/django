from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm, CreateUserForm
from dashboard.models import UserProfile
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/');

    user = request.user
    profile = UserProfile.objects.get(base_user=user)
    data = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'dashboard/home.html', data)

def newuser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = CreateUserForm()
        data = {
            'form': form,
            'user': request.user,
        }
        return render(request, 'dashboard/newuser.html', data)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('/');

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('../home/')
    else:
        profile = UserProfile.objects.get(base_user=request.user)
        form = EditProfileForm(initial={
            'base_crypto': profile.base_crypto,
            'base_fiat': profile.base_fiat,
            'first_name': profile.base_user.first_name,
            'last_name': profile.base_user.last_name,
            'email': profile.base_user.email,
            })
        data = {
            'form': form,
            'user': request.user
        }
        return render(request, 'dashboard/editprofile.html', data)