from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # Asegúrate de que esta línea esté incluida
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bodega, Vino, Reseña, Page, Profile
from .forms import BodegaForm, VinoForm, ReseñaForm, PageForm, ProfileForm

# Página de inicio
def inicio(request):
    return render(request, 'vinos/inicio.html')

# Vista de registro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Te has registrado con éxito! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()
    return render(request, 'vinos/signup.html', {'form': form})

# Crear una bodega
def crear_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'vinos/exito.html')
    else:
        form = BodegaForm()
    return render(request, 'vinos/formulario.html', {'form': form, 'titulo': 'Nueva Bodega'})

# Buscar un vino
def buscar_vino(request):
    query = request.GET.get('q')
    resultados = Vino.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'vinos/buscar.html', {'resultados': resultados})

# Acerca de mí
def about(request):
    return render(request, 'vinos/about.html')

# Listado de páginas
class PageListView(ListView):
    model = Page
    template_name = 'vinos/pages.html'
    context_object_name = 'paginas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['no_hay_paginas'] = not self.object_list.exists()
        return context

# Detalle de una página
class PageDetailView(DetailView):
    model = Page
    template_name = 'vinos/page_detail.html'
    context_object_name = 'pagina'

# Crear una página (requiere login)
class PageCreateView(LoginRequiredMixin, CreateView):  # Esta clase ahora debería funcionar sin errores
    model = Page
    form_class = PageForm
    template_name = 'vinos/page_form.html'
    success_url = reverse_lazy('pages')

# Editar una página (requiere login)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'vinos/page_form.html'
    success_url = reverse_lazy('pages')

# Borrar una página (requiere login)
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'vinos/page_confirm_delete.html'
    success_url = reverse_lazy('pages')

# Perfil del usuario
@login_required
def profile(request):
    return render(request, 'vinos/profile.html')

# Editar perfil del usuario
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'vinos/edit_profile.html', {'form': form})

