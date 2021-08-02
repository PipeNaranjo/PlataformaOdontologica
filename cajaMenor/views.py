from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from citas.models import Evento
from pedidos.models import Producto

# Create your views here.


class CajaVista(TemplateView,LoginRequiredMixin):
    template_name="cajamenor/cajamenor.html"
    login_url='accounts/login/'
    redirect_field_name='cajamenor/cajamenor.html'
    models = Evento,Producto

    def post(self,request,*args,**kwargs):

        fecha = request.POST.get('fecha')
        citas = Evento.objects.filter(start=fecha)
        productos = Producto.objects.filter(fechaRegistro=fecha)
        error =""
        if not citas and not productos:
            error = "No hay ningún registro en la fecha %s" %fecha
        else:
            totalP = 0
            totalC = 0
            for prd in productos:
                totalP = totalP + prd.precio
            for cita in citas:
                totalC = totalC + int(cita.precio)

            
            mensaje=str(totalC-totalP)

        return render(request,self.template_name,{'citas':citas,'productos':productos,'error':error,'mensaje':mensaje})