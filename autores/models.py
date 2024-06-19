from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=128)
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.name
    
class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    sinopsis = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    
    def __str__(self):
        return self.titulo