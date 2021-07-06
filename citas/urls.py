from django.urls import path
from .views import citas

urlpatterns=[
    path('',citas,name="citas"),
]