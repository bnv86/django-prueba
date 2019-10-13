from django.db import models

# Create your models here.

class Persona(models.Model):
    #folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        #esto es para que retorne nombre y apellido en lugar del objeto
        return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.SET_NULL)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()

    def __str__(self):
        #esto es para que retorne el nombre completo de la persona y el id de la solicitud en lugar del objeto
        if ('{}'.format(self.persona) == 'None'):
            return '{}'.format(self.id) + ' de ' + 'ANONIMO'
        else:
            return '{}'.format(self.id) + ' de ' + '{}'.format(self.persona)
        