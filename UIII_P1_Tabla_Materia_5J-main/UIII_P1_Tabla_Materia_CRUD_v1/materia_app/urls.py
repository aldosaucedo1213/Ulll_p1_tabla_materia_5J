from django.urls import path
from materia_app import views
urlpatterns = [
    path("",views.Inicio_Vista, name="Inicio_Vista")
]
