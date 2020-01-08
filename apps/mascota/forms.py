from django import forms
from apps.mascota.models import Mascota, User, Vacuna
from django.contrib.auth.models import User

class MascotaForm(forms.ModelForm):

    
    vacunas = forms.ModelMultipleChoiceField(
            queryset=Vacuna.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
        
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'usuario',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'usuario': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}), #tiene que quedar fijo el usuario logueado
            'vacuna': forms.CheckboxSelectMultiple(),
        }