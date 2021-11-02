
from .views import RegisterAPI, LoginAPI, ChangePasswordView
from knox import views as knox_views
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('logout/', knox_views.LogoutView.as_view(), name="logout"),
    path('logoutall/', knox_views.LogoutView.as_view(), name="logoutall"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', include('django_rest_passwordreset.urls'),
         name='password-reset'),

]
