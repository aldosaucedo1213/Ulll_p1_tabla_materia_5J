from django.urls import path
from materia_app import views
urlpatterns = [
    path("",views.Inicio_Vista, name="Inicio_Vista"),
    path("registrarmateria/",views.registrarmateria,name="registrarmateria"),
    path("seleccionarmateria/<Codigo>",views.seleccionarmateria,name="seleccionarmateria"),
    path("editarmateria",views.editarmateria,name="editarmateria"),
    path("borrarmateria/<Codigo>",views.borrarmateria,name="borrar")
    
    
]
