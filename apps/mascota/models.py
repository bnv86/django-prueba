from django.db import models

from apps.adopcion.models import Persona, Solicitud

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        #esto es para que retorne el nombre de la vacuna en administracion (no el objeto)
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    #folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    
    #ATRIBUTO QUE RELACIONA Mascota/Persona
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    #ATRIBUTO QUE RELACIONA LOS DOS MODELOS (Mascota/Vacuna)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        #esto es para que retorne el nombre de la mascota en administracion (no el objeto)
        return '{}'.format(self.nombre)

