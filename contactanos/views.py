from django.shortcuts import render

# Create your views here.

def contactanos(request):
    return render(request,"contactanos/contactanos.html")