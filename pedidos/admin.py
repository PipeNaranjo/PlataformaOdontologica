from pedidos.models import Producto
from django.contrib import admin

# Register your models here.

class AdminInven(admin.ModelAdmin):
    list_display=('codigo','descripcion','peso','cantidad','fechaCaducidad','fechaRegistro','precio','estado')

admin.site.register(Producto,AdminInven)