from django.shortcuts import render
# Create your views here.
def catcher(request):

    data = {
        'name': ''
    }
    return render(request, 'dashboard/index.html', data)
