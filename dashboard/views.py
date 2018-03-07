from django.shortcuts import render
# Create your views here.
def catcher(request):

    data = {
        'name': 'I\'m The Name'
    }
    return render(request, 'dashboard/index.html', data)
