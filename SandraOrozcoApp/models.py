from django.db import models
from django.db.models.fields import BooleanField, CharField, EmailField

# Create your models here.

class Usuario(models.Model):
    correo=EmailField(blank=False,null=False)
    contrasena=CharField(max_length=10,blank=False,null=False)
    login=BooleanField(blank=False,null=False,default=False)

    class Meta():
        verbose_name='usuario'
        verbose_name_plural='usuarios'

