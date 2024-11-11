from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.

def Inicio_Vista(request):
    lasMaterias=Materia.objects.all()
    return render(request, "GestionarMateria.html",{"mismaterias":lasMaterias})

def registrarmateria(request):
    Codigo=request.POST["txtCodigo"]
    Nombre=request.POST["txtNombre"]
    Creditos=request.POST["numCreditos"]

    guardarmateria=Materia.objects.create(
        Codigo=Codigo,Nombre=Nombre,Creditos=Creditos
    ) #guarda el registro

    return redirect("/")