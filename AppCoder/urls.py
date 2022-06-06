from django.urls import path
from AppCoder.views import curso, cursos, entregables, estudiantes, inicio,profesores

urlpatterns = [
    path('profesores/',profesores),
    path('curso/',curso),
    path('',inicio),
    path('estudiantes/',estudiantes),
    path('entregables/',entregables),
    path('cursos/',cursos),
    
]
