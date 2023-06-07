from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
# This is a Django model class for a book with fields for id, title, image, and description.

class Libro(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length = 100, verbose_name = "Titulo", null= True)
    imagen = models.ImageField(upload_to = "imagenes/", verbose_name = "Imagen", null = True)
    descripción  = models.TextField(verbose_name = "Descripción", null= True)
                                                                # no puede ser nulo

    
    def __str__(self):
       
        row = "Titulo: " +self.titulo + " | " +  " Descripción: " + self.descripción
        return row
    
    def delete(self, using=None, keep_parents=False):
        
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
# Modelo donde se almacenara la informacion
# Nos funionara para atrapar toda la estructura de la tabla libros.

""" Se debe incluir ciertas condiciones en la consola, para actualizar la base de datos
    Se debe hacer la migración, la generacion de toda la estructura necesaria, se analizara el modelo, se descompone, y actualizan la base de datos
    En consola escribimos python manage.py makemigrations,
    Luego se debe migrar la informacion a la base de datos, por lo que escribimos en consola python manage.py migrate
    se treparan todos los datos a la base de datos"""

