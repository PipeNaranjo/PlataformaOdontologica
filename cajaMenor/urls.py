from cajaMenor.views import CajaVista
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns=[
    path('',login_required(CajaVista.as_view()),name="cajaMenor"),
]