from django.db import models

# Create your models here.

class Evento(models.Model):

    nombre = models.CharField(max_length=50,blank=False,null=False)
    email= models.CharField(max_length=50,blank=False,null=False)
    celular=models.CharField(max_length=10,blank=True,null=True)
    start=models.DateTimeField(blank=False,null=False)
    end=models.DateTimeField(blank=False,null=False)
    created=models.DateTimeField(auto_now_add=True) #Crea la fecha automaticamente
    updated=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='evento'
        verbose_name_plural='eventos'

    def __str__(self):
        return "Paciente: %s, Fecha cita: %s" %(self.nombre, self.fecha)