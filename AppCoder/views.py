from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.

def curso(self):
    curso = Curso(nombre = "noni", camada ="1544")
    curso.save()
    documentoDeTexto = f"----->Curso: {curso.nombre},  Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

def inicio(self):
    documento = ('Vista inicio. Las opciones son: <br> cursos, estudiantes, entregables, profesores')
    return HttpResponse(documento)

def cursos(self):
    return HttpResponse ('vista cursos')

def estudiantes(self):
    return HttpResponse('vista estudiantes')

def entregables(self):
    return HttpResponse('vista entregables')

def profesores(self):
    documento = "Pagina de profesores"
    return HttpResponse(documento)