from django import forms


class Formulario_Evento(forms.Form):
    nombre=forms.CharField(label="Nombre paciente",required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    fecha=forms.CharField(label="Fecha", required=True)
    hora=forms.CharField(label="Hora",required=True,widget=forms.TextInput(attrs={'placeholder': 'Formato 00:00'}))
    celular=forms.CharField(label="Celular",required=True,widget=forms.TextInput(attrs={'placeholder': 'Celular'}))
    email=forms.EmailField(label="Email contacto",required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}))

