from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class Usuario(models.Model):
    correo=EmailField(blank=False,null=False)
    contraseña=CharField(max_length=10,blank=False,null=False)

    class Meta():
        verbose_name='usuario'
        verbose_name_plural='usuarios'

