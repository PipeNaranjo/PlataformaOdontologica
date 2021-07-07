
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario


# Create your views here.

def home(request):
    '''
    usuario=Usuario.objects.all()
    if not usuario.exists():
        Usuario.objects.create(correo="andresnaranjo3098@hotmail.com", contrasena="andres3098")


    if request.method == 'POST':

        usuario=Usuario.objects.get(id=1)
        

        if usuario.correo==request.POST.get("correo") and usuario.contrasena==request.POST.get("password"):

            usuario.login=True
    '''
    return render(request,"SandraOrozcoApp/home.html")
