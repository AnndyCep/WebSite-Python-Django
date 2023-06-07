from django import forms
# Vamos a utilizar los formularios
from .models import Libro
# Requerimos formulario apartir de un modelo

# This is a Django form class for the Libro model that includes all fields.
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        # Estos datos son importantes, porque con esto se realiza la lectura y el mapeado

