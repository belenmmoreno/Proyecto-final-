from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Para el texto enriquecido


# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre


class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()  
    def __str__(self):
        return self.nombre

    
class Reseña(models.Model):
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    def __str__(self):
        return f'Reseña de {self.usuario} sobre {self.vino}'
    
class Page(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField()  # Usamos el campo RichTextField para texto enriquecido
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
     
    def _str_(self):
        return self.titulo
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default="Sin nombre")
    apellido = models.CharField(max_length=100, default="Sin apellido")
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    
    def _str_(self):
        return self.user.username
