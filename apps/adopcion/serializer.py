from rest_framework.serializers import ModelSerializer
from apps.adopcion.models import Solicitud, Persona

class SolicitudSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('usuario', 'numero_mascotas', 'razones', 'created_at', 'updated_at')

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'edad', 'telefono', 'email', 'domicilio', 'created_at', 'updated_at')

