from django.db import models

# Create your models here.

estados = [('Verde', 'Verde'),('Amarillo','Amarillo'),('Rojo','Rojo')]
class Producto(models.Model):
    codigo=models.CharField(max_length=50,blank=False,null=False,unique=True)
    descripcion=models.CharField(max_length=80,blank=True,null=True)
    cantidad=models.IntegerField(blank=False,null=False)
    peso=models.IntegerField(blank=True,null=False)
    medida=models.CharField(max_length=20,blank=False,null=False,default="Gramos")
    fechaCaducidad=models.DateField(blank=False,null=False)
    fechaRegistro=models.DateField(blank=False,null=False)
    precio=models.IntegerField(blank=False,null=False)
    estado=models.CharField(max_length=10,choices=estados,blank=False,null=False)

    class Meta():
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.descripcion

    def save(self,*args,**kwargs):
        fechaC=str(self.fechaCaducidad).split('-')
        fechaR=str(self.fechaRegistro).split('-')
        print(fechaR)
        if int(fechaC[0]) - int(fechaR[0]) >= 1:
            self.estado="Verde"
        elif int(fechaC[1]) - int(fechaR[1]) <= 6 and int(fechaC[1]) - int(fechaR[1]) > 3:
            self.estado="Amarillo"
        elif int(fechaC[1]) - int(fechaR[1]) <= 3:
            self.estado="Rojo"
        
        super().save(*args,**kwargs)
