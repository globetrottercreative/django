from django.shortcuts import render, redirect
from .forms import SearchForm, RegistrationForm
from dashboard.models import UserProfile
# Create your views here.
def catcher(request):
    form = SearchForm()
    user = UserProfile.objects.all()
    print(user)
    data = {
        'name': 'I\'m The Name',
        'form': form,
        'id_name': user
    }
    return render(request, 'dashboard/search.html', data)


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