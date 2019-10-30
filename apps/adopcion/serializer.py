from rest_framework.serializers import ModelSerializer
from apps.adopcion.models import Solicitud, Persona
from django.contrib.auth.models import User

#para relacion uno a uno con la solicitud
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SolicitudSerializer(ModelSerializer):
    #para relacion uno a uno con la solicitud
    #user = UserSerializer(read_only=True)
    class Meta:
        model = Solicitud
        fields = ('usuario', 'numero_mascotas', 'razones', 'created_at', 'updated_at')

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'edad', 'telefono', 'email', 'domicilio', 'created_at', 'updated_at')

