from rest_framework.serializers import ModelSerializer
from apps.mascota.models import Mascota, Vacuna

class MascotaSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre', 'sexo', 'edad_aproximada', 'fecha_rescate', 'created_at', 'updated_at')


class VacunaSerializer(ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('nombre', 'created_at', 'updated_at')