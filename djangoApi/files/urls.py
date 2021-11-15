
from django.urls import path, include
from . import views

urlpatterns = [
    path('download/<str:file_name>/', views.download_file, name="download_file"),
    path('downloadimage/<str:file_name>/',
         views.download_image, name="download_image"),
    path('tube/', views.download_tube, name="download_tube"),
]
