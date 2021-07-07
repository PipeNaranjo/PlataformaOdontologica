
from SandraOrozcoApp.views import home
from django.urls import path


urlpatterns = [
    path('', home, name='Home'),
]