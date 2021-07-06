from django.urls import path
from .views import informacion

urlpatterns=[
    path('',informacion,name="informacion"),
]