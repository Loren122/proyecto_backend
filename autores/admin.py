from django.contrib import admin
from autores.models import Autor, Libro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)