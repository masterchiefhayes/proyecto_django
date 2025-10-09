from django.contrib import admin

from .models import Estudiante, Administrador, Publicacion, Comentario

admin.site.register(Estudiante)
admin.site.register(Administrador)
admin.site.register(Publicacion)
admin.site.register(Comentario)
