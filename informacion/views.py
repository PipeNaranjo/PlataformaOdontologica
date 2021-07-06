from django.shortcuts import render

# Create your views here.

def informacion(request):
    return render(request, "informacion/seccion1.html")