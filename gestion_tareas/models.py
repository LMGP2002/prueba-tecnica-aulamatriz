from django.db import models
from django.contrib.auth.models import User


# Clase que crea la estructura de la tabla tarea en la BD

class Tarea(models.Model):
    prioridad_opciones=[('baja','Baja'),('media','Media'),('alta','Alta')]

    titulo=models.CharField(max_length=200)
    descripcion=models.TextField(null=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_limite=models.DateTimeField()
    prioridad=models.CharField(choices=prioridad_opciones, default='alta', max_length=5)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo