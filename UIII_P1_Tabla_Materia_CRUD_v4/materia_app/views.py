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
def seleccionarmateria(request,Codigo):
    materia=materia.objects.get(Codigo=Codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarmateria(request):
    Codigo=request.POST["txtCodigo"]
    Nombre=request.POST["txtNombre"]
    Creditos=request.POST["numCreditos"]
    materia=Materia.objects.get(Codigo=Codigo)
    materia.Nombre=Nombre
    materia.Creditos=Creditos
    materia.save() #guarda registro actualizado
    return redirect("/")

def  borrarmateria(request,Codigo):
    materia=Materia.objects.get(Codigo=Codigo)
    materia.delete() # borra el registro
    return redirect("/")