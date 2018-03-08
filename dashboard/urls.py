from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.catcher, name='catch'),
    url(r'^login/$', login, {'template_name': 'dashboard/login.html'}),
]