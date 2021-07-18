from django.urls import path
from .views import Vista

urlpatterns=[
    path('',Vista.as_view(),name="citas"),
]