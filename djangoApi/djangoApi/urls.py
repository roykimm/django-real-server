
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from gallery.views import GalleryView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", GalleryView, basename="galleyview")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginapi/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('file/', include('files.urls')),
    path('gallery/', include(route.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
