from django.urls import path
from .views import IVista

urlpatterns=[
    path('',IVista.as_view(),name="inventario"),
]