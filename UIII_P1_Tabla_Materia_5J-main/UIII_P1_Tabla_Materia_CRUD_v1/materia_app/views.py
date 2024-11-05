from django.shortcuts import render
from .models import Materia
# Create your views here.

def Inicio_Vista(request):
    lasMaterias=Materia.objects.all()
    return render(request, "GestionarMateria.html")