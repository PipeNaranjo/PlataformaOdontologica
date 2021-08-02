import datetime
from pedidos.models import Producto
from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class IVista(TemplateView,LoginRequiredMixin):
    template_name='pedidos/inventario.html'
    model=Producto
    login_url='accounts/login/'
    redirect_field_name='pedidos/inventario.html'

    def get(self,request,*args,**kwargs):
        prods = self.model.objects.all()
        return render(request,self.template_name,{"productos":prods})

    def post(self,request,*args,**kwargs):
        try:
            cod=request.POST.get("codigo")
            desc=request.POST.get("descripcion")
            cant=request.POST.get("cantidad")
            pe=request.POST.get("peso")
            fechaC=request.POST.get("fecha")
            fechaR=datetime.datetime.now()
            pre=request.POST.get("precio")

            prod = self.model.objects.filter(codigo=cod)
            if prod:
                error = "Ya existe el producto con el codigo %s"%cod
                prods = self.model.objects.all()
                return render(request,self.template_name,{"error":error,"productos":prods})
            else:
                self.model.objects.create(codigo=cod,descripcion=desc,cantidad=cant,peso=pe, fechaCaducidad=fechaC, precio=pre, fechaRegistro=fechaR)
                prods = self.model.objects.all()
                return render(request,self.template_name,{"productos":prods})
        except ValueError as e:
            error = "Valor incorrecto en un campo del formulario"
            prods = self.model.objects.all()
            return render(request,self.template_name,{"error":error,"productos":prods})

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('inventario')

        



    
    
