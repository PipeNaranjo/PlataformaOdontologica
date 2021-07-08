from citas.forms import FormularioEvento
from django.shortcuts import render
from citas.models import Evento

# Create your views here.

def citas(request):

    form =FormularioEvento()

    if request.method == 'POST':
        form=FormularioEvento(data=request.POST)

        if form.is_valid():
            n=request.POST.get("nombre")
            f=request.POST.get("fecha")
            h=str(request.POST.get("hora"))
            e=request.POST.get("email")
            c=request.POST.get('celular')
            horas=h.split(sep=':')
            minutos=int(horas[1])
            minutos = minutos+15
            
            if minutos >= 60:
                min="00"
            else:
                min=str(minutos)

            final=f+ " " + horas[0]+":"+min

            evento = Evento.objects.create(nombre=n,start=f+" "+h,end=final,email=e,celular=c)



    return render(request,"citas/calendario.html",{"formulario":form})