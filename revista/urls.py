from django.urls import path
from .views import (
    EstudianteListView, EstudianteDetailView, EstudianteUpdateView,
    AdministradorListView, AdministradorDetailView, AdministradorUpdateView,
    PublicacionListView, PublicacionDetailView, PublicacionUpdateView,
    HomeView, AcercaView, EstudianteRegistroView, EstudianteLogoutView
)

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),

    # Estudiantes
    path('estudiantes/', EstudianteListView.as_view(), name='estudiantes-list'),
    path('estudiante/<int:pk>/', EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('estudiante/<int:pk>/edit/', EstudianteUpdateView.as_view(), name='estudiante-edit'),

    # Administradores
    path('administradores/', AdministradorListView.as_view(), name='administradores-list'),
    path('administrador/<int:pk>/', AdministradorDetailView.as_view(), name='administrador-detail'),
    path('administrador/<int:pk>/edit/', AdministradorUpdateView.as_view(), name='administrador-edit'),

    # Publicaciones
    path('publicaciones/', PublicacionListView.as_view(), name='publicaciones-list'),
    path('publicacion/<int:pk>/', PublicacionDetailView.as_view(), name='publicacion-detail'),
    path('publicacion/<int:pk>/edit/', PublicacionUpdateView.as_view(), name='publicacion-edit'),

    # Páginas estáticas
    path('acerca/', AcercaView.as_view(), name='acerca'),

    # Registro y Logout de estudiantes
    path('registro/', EstudianteRegistroView.as_view(), name='registro'),  #  Registro
    path('logout/', EstudianteLogoutView.as_view(), name='logout'),
]
