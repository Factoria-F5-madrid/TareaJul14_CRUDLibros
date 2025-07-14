from django.db import models

# Create your models here.
from django.db import models

class Libro(models.Model): # Creo la entidad libro, cuyos atributos son: titulo, autor, descripcion, fecha de publi y un ISBN
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self): # Metodo para devolver el propio libro (preguntar: cuenta como constructor?)
        return self.titulo