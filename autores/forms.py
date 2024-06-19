from django import forms

from autores.models import Autor, Libro

# def validate_number(value):
#     if not isinstance(value, int):
#         raise ValidationError("El numero debe ser un número entero.")
#     if value > -1:
#         raise ValidationError("El año de aparición debe tener exactamente 4 dígitos.")



class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = [
            'name',
            'biografia',
            'fecha_nacimiento',
        ]

class LibroForm(forms.ModelForm):
    
    class Meta:
        model =  Libro
        fields = [
            'titulo',
            'autor',
        ]