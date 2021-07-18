from django.contrib import admin
from .forms import FormularioEvento
from .models import Evento

# Register your models here.

class CitasAdmin(admin.ModelAdmin):
    
    list_display=('nombre','start','end','horaInicio','horaFinal','email','celular','created','updated')

admin.site.register(Evento,CitasAdmin)