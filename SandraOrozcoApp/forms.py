
from django import forms

class Formulario_Ingreso(forms.Form):
    
    correo=forms.EmailField(label="Correo",required=True)
    password=forms.CharField(label="Contraseña",required=True)