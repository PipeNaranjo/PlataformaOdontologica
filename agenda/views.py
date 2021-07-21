from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,FormView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from citas.models import Evento
from .forms import FormularioEvento

# Create your views here.


class Agenda(FormView,TemplateView,LoginRequiredMixin):
    template_name='agenda/calendario.html'
    models = Evento
    form_class=FormularioEvento
    login_url ='accounts/login/'

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        eventos = Evento.objects.all()
        return render(request, self.template_name, {'form':form,'object_list':eventos})

    def post(self,request,*args, **kwargs):
        mensaje=''
        error=False
        form = self.form_class(request.POST)
        if form.is_valid():
            n=request.POST.get("nombre")
            f=request.POST.get("fecha")
            h=request.POST.get("hora")
            e=request.POST.get("email")
            c=request.POST.get('celular')
            p=request.POST.get('precio')

            eventos = self.models.objects.filter(start=f)
            ward = True
            for evento in eventos:
                if evento.horaInicio == h:
                    ward =False
            evento = self.models.objects.filter(nombre=n,email=e)
            if evento :
                evento[0].precio=p
                evento[0].save()
            else:
                if ward:
                    self.models.objects.create(nombre=n,start=f,horaInicio=h,email=e,celular=c,precio=p)
                    mensaje= 'Registro exitoso'
                    
                else:
                    error = True
                    mensaje='La hora %s no esta disponible en la fecha %s' %(h,f)
        form = self.form_class()
        eventos=Evento.objects.all()
        return render(request, self.template_name, {'form':form,'mensaje':mensaje,'error':error,'object_list':eventos})




