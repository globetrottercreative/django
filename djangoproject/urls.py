
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('posts.urls')),
    path('dash/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)