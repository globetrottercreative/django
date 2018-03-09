from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'dashboard/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'dashboard/logout.html'}),
    url(r'^home/$', views.home, name='search_crypto'),
    url(r'^edit/$', views.edit, name='edit_profile'),
    url(r'^register/$', views.registration, name='registration'),
]