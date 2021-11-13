
from django.urls import path, include
from . import views

urlpatterns = [
    path('download/<str:file_name>/', views.download_file, name="download_file"),
    path('downloadimage/<str:file_name>/',
         views.download_image, name="download_image"),
    #path('tube/<str:url>/', views.download_file, name="download_file"),
]
