from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello From Posts')
    return render(request, 'posts/index.html', {
        'title': 'Latests Posts'
    })

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)