from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup'),
    path('inicio/', views.inicio, name='inicio'),
    path('crear_bodega/', views.crear_bodega, name='crear_bodega'),
    path('buscar_vino/', views.buscar_vino, name='buscar_vino'),
    path('about/', views.about, name='about'),
    path('pages/', views.PageListView.as_view(), name='pages'),
    path('pages/<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/edit/<int:pk>/', views.PageUpdateView.as_view(), name='page_edit'),
    path('pages/delete/<int:pk>/', views.PageDeleteView.as_view(), name='page_delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

