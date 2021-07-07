from django.urls import path
from .views import contactanos

urlpatterns=[
    path('',contactanos,name="contactanos"),
]