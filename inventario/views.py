from inventario.models import Producto
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IVista(View,LoginRequiredMixin):
    template_name='inventario/inventario.html'
    model=Producto
    login_url='accounts/login/'
    redirect_field_name='inventario/inventario.html'

    def get(self,request,*args,**kwargs):
        productos=self.model.objects.all()
        return render(request,self.template_name,{"productos":productos})

    def post(self,request,*args,**kwargs):
        
            cod=request.POST.get("codigo")
            desc=request.POST.get("descripcion")
            cant=request.POST.get("cantidad")
            pe=request.POST.get("peso")
            fechaC=request.POST.get("fecha")
            pre=request.POST.get("precio")

            self.model.objects.create(codigo=cod,descripcion=desc,cantidad=cant,peso=pe, fechaCaducidad=fechaC, precio=pre)

            prods = self.model.objects.all()
            return render(request,self.template_name,{"productos":prods})
        