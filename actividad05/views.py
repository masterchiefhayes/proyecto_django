from django.shortcuts import render

# Página Home
def home(request):
    return render(request, 'actividad05/home.html')

# Página Estudiantes
def estudiantes(request):
    return render(request, 'actividad05/estudiantes.html')

# Página Administradores
def administradores(request):
    return render(request, 'actividad05/administradores.html')

# Página Acerca de
def acerca(request):
    return render(request, 'actividad05/acerca.html')
