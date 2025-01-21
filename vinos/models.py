from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Para el texto enriquecido

# Modelo para la Bodega
class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para el Vino
class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para la Reseña
class Reseña(models.Model):
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f'Reseña de {self.usuario} sobre {self.vino}'

# Modelo para las Páginas con contenido enriquecido
class Page(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField()  # Usamos el campo RichTextField para texto enriquecido
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Modelo para el Perfil del Usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    nombre = models.CharField(max_length=100, default="Sin nombre")  # Nombre del usuario
    apellido = models.CharField(max_length=100, default="Sin apellido")  # Apellido del usuario
    email = models.EmailField()  # Email del perfil (puedes usar el email del User también)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Avatar del usuario
    biografia = models.TextField(null=True, blank=True)  # Biografía del usuario

    def __str__(self):
        return self.user.username  # El nombre del perfil será el nombre de usuario

# Señales para crear y guardar el perfil al crear o actualizar un usuario
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Si el usuario es creado
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Guarda los cambios en el perfil
