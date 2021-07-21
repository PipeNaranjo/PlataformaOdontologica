from agenda.views import Agenda
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns=[
    path('',login_required(Agenda.as_view()),name="agenda"),
]