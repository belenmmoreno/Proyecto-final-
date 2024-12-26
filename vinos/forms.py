from django import forms
from .models import Bodega, Vino, Reseña, Page, Profile

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'ubicacion', 'descripcion']  # Lista de campos específicos o usa '_all_' para incluir todos


class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = ['nombre', 'bodega', 'tipo', 'precio', 'descripcion']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['usuario', 'vino', 'comentario', 'calificacion']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'contenido', 'imagen']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'email', 'avatar', 'biografia']
