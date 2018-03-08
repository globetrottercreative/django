from django.shortcuts import render
from .forms import SearchForm
from dashboard.models import UserProfile
# Create your views here.
def catcher(request):
    form = SearchForm()
    user = UserProfile.objects.all()
    data = {
        'name': 'I\'m The Name',
        'form': form,
        'id_name': user.username
    }
    return render(request, 'dashboard/search.html', data)


