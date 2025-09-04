from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
    path('acerca/', views.acerca, name='acerca'),
]
