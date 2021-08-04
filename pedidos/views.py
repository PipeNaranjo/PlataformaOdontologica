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
            med=request.POST.get("medida")
            fechaC=request.POST.get("fecha")
            fechaR=datetime.datetime.now()
            pre=request.POST.get("precio")
            error = False
            if med == '--seleccione medida--':
                mensaje = "Medida incorrecta"
                error = True
                prods = self.model.objects.all()
                return render(request,self.template_name,{"error":error,"productos":prods, "mensaje":mensaje})
            prod = self.model.objects.filter(codigo=cod)
            if prod:
                mensaje = "Ya existe el producto con el codigo %s"%cod
                prods = self.model.objects.all()
                error = True
                return render(request,self.template_name,{"error":error,"productos":prods,"mensaje":mensaje})
            else:
                self.model.objects.create(codigo=cod,descripcion=desc,cantidad=cant,peso=pe, fechaCaducidad=fechaC, precio=pre, fechaRegistro=fechaR,medida=med)
                prods = self.model.objects.all()
                mensaje="Pedido Registrado"
                return render(request,self.template_name,{"productos":prods,"mensaje":mensaje,"error":error})
        except ValueError as e:
            mensaje = "Valor incorrecto en un campo del formulario"
            prods = self.model.objects.all()
            error = True
            return render(request,self.template_name,{"error":error,"productos":prods,"mensaje":mensaje})

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('inventario')

        



    
    
