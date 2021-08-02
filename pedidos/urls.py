from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IVista, EliminarProducto

urlpatterns=[
    path('',login_required(IVista.as_view()),name="inventario"),
    path('producto_confirm_delete/<int:pk>',EliminarProducto.as_view(),name='eliminarProducto'),
]