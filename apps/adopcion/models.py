from django.db import models
from apps.usuario.models import User
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    #folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #esto es para que retorne nombre y apellido en lugar del objeto
        return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user = models.OneToOneField(User) #relacion uno a uno de solicitud con usuario, luego de esto hay que hacer makemigrations con la opc 1, luego migrate

    def __str__(self):
        #esto es para que retorne el nombre completo de la persona y el id de la solicitud en lugar del objeto
        if ('{}'.format(self.usuario) == 'None'):
            return '{}'.format(self.id) + ' de ' + 'ANONIMO'
        else:
            return '{}'.format(self.id) + ' de ' + '{}'.format(self.usuario)
        