from django.db import models

from apps.adopcion.models import Persona, Solicitud, User
from django.contrib.auth.models import User

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #esto es para que retorne el nombre de la vacuna en administracion (no el objeto)
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    #folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #ATRIBUTO QUE RELACIONA Mascota/Persona
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    #ATRIBUTO QUE RELACIONA LOS DOS MODELOS (Mascota/Vacuna)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        #esto es para que retorne el nombre de la mascota en administracion (no el objeto)
        return '{}'.format(self.nombre)

