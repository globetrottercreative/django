from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    
    posts = Posts.objects.all()[:10]

    data = {
        'title': 'My DEV Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', data)