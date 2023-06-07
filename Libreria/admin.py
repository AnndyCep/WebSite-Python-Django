from django.contrib import admin
from .models import Libro
# Importa el modelo que es libro
# Register your models here.

# Se debe regristar
admin.site.register(Libro) # Se registra el modelo, para cuando se corra el admin, pueda manipular el libro


