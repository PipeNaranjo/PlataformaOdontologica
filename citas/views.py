from citas.forms import FormularioEvento
from django.shortcuts import render
from django.views.generic import ListView,FormView,TemplateView
from citas.models import Evento

# Create your views here.

class Vista(FormView,TemplateView):
    model = Evento
    template_name='citas/calendario.html'
    form_class = FormularioEvento
    success_message='Se registro con exito el evento'

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

            eventos = self.model.objects.filter(start=f)
            ward = True
            for evento in eventos:
                if evento.horaInicio == h:
                    ward =False

            if ward:
                self.model.objects.create(nombre=n,start=f,horaInicio=h,email=e,celular=c)
                mensaje= 'Registro exitoso'
                
            else:
                error = True
                mensaje='La hora %s no esta disponible en la fecha %s' %(h,f)
        form = self.form_class()
        eventos=Evento.objects.all()
        return render(request, self.template_name, {'form':form,'mensaje':mensaje,'error':error,'object_list':eventos})


    

