from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]
    data = {
        'title': 'My DEV Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', data)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)