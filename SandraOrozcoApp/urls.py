
from SandraOrozcoApp.views import home
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='Home'),
]