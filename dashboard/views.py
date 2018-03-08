from django.shortcuts import render
from .forms import SearchForm
# Create your views here.
def catcher(request):

    form = SearchForm()

    data = {
        'name': 'I\'m The Name',
        'form': form
    }
    return render(request, 'dashboard/search.html', data)


