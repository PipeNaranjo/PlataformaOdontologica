from citas.models import Evento
from django import forms

horas=[("7:00","7:00"),("7:15","7:15"),("7:30","7:30"),("7:45","7:45"),("8:00","8:00"),("8:15","8:15"),("8:30","8:30"),("8:45","8:45"),("9:00","9:00")
,("9:15","9:15"),("9:30","9:30"),("9:45","9:45"),("10:00","10:00"),("10:15","10:15"),("10:30","10:30"),("10:45","10:45"),("11:00","11:00")
,("11:15","11:15"),("11:30","11:30"),("11:45","11:45"),("12:00","12:00"),("12:15","12:15"),("12:30","12:30"),("12:45","12:45"),("13:00","13:00")
,("13:15","13:15"),("13:30","13:30"),("13:45","13:45"),("14:00","14:00"),("14:15","14:15"),("14:30","14:30"),("14:45","14:45"),("15:00","15:00")
,("15:15","15:15"),("15:30","15:30"),("15:45","15:45"),("16:00","16:00"),("16:15","16:15"),("16:30","16:30"),("16:45","16:45")]

class FormularioEvento(forms.Form):
    
    nombre=forms.CharField(label="Nombre paciente",required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    fecha=forms.CharField(label="Fecha",required=True)
    hora=forms.ChoiceField(label="Hora",choices=horas)
    celular=forms.CharField(label="Celular",required=True,widget=forms.TextInput(attrs={'placeholder': 'Celular'}))
    email=forms.EmailField(label="Email contacto",required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    