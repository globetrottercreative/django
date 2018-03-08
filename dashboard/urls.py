from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', login, {'template_name': 'dashboard/login.html'}),
    url(r'^home/$', views.catcher, name='search_crypto'),
    url(r'^edit/$', views.edit, name='edit_profile'),
    url(r'^register/$', views.registration, name='registration'),
]