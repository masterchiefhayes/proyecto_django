from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    carne = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    carne = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    autorizado_por = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.estudiante.nombre} en {self.publicacion.titulo}"
