from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'dashboard/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'dashboard/logout.html'}),
    url(r'^home/$', views.home, name='search_crypto'),
    url(r'^newuser/$', views.newuser, name='new_user'),
    url(r'^editprofile/$', views.editprofile, name='edit_profile'),
    url(r'^home/refresh/$', views.refresh_crypto, name='refresh'),
]