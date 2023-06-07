from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.


def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all() # Utilizamos el modelo, usamos toda la informacion
    return render(request,'libros/index.html', { "libros":libros})

def crear(request):

    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): # Condicional si se realiza una validacion
        formulario.save() # Se guanda la informacion
        return redirect("libros") # Se redicciona a libros
    return render(request,'libros/crear.html', { "formulario": formulario})

def editar(request, id):
    
    libro = Libro.objects.get(id=id) # Estamos creando la consulta de libro a traves de get.
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)# Se la estamos pasando para que nos muestre los datos
    if formulario.is_valid and request.POST: # Condicional si se valida y despues hay un envio
        formulario.save() # se guarda la informacion
        return  redirect("libros")
    return render(request,'libros/editar.html',{"formulario":formulario})
    # Ya con esto permite editar.

def eliminar(request, id):
    
    libro = Libro.objects.get(id = id) # Realiza la consulta del Id con el get
    libro.delete() 
    return redirect("libros") # Redicciona a libros