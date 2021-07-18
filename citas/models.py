from datetime import timedelta
from django.db import models
from django.forms.fields import Field
from SandraOrozco import settings

# Create your models here.


class Evento(models.Model):

    nombre = models.CharField(max_length=50,blank=False,null=False)
    email= models.CharField(max_length=50,blank=False,null=False)
    celular=models.CharField(max_length=10,blank=True,null=True)
    start=models.DateField(blank=False,null=False)
    horaInicio=models.CharField(max_length=5,blank=False,null=False)
    horaFinal=models.CharField(max_length=5,blank=False,null=False,default="00:00")
    end=models.DateField(blank=False,null=False)
    created=models.DateField(auto_now_add=True) #Crea la fecha automaticamente
    updated=models.DateField(auto_now_add=False, auto_now=True)

    class Meta():
        verbose_name='evento'
        verbose_name_plural='eventos'

    def __str__(self):
        return "Paciente: %s, Fecha cita: %s" %(self.nombre, self.start)

    def save(self,*args,**kwargs):

        horas = str(self.horaInicio).split(":")
        if int(horas[1])+15 == 60:
            min="00"
            hour=str(int(horas[0])+1)
        else:
            min=str(int(horas[1])+15)
            hour=horas[0]

        self.horaFinal=hour+":"+min
        self.end = self.start
        super().save(*args,**kwargs)
