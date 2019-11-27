from django import forms
from django.forms import ModelForm
from apps.adopcion.models import Persona, Solicitud
from apps.usuario.models import User
from django.contrib.auth.models import User

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),
        }

class SolicitudForm(forms.ModelForm):

    class Meta:

        model = Solicitud
        
        fields = [
            'usuario',
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'usuario': 'Usuario',
            'numero_mascotas': 'Numero de mascotas',
            'razones': 'Razones para adoptar',
        }
        widgets = {
            'usuario':forms.Select(attrs={'class':'form-control'}), #tiene que quedar fijo el usuario logueado
            'numero_mascotas': forms.NumberInput(attrs={'class':'form-control', 'min': 1, 'max': 5}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }

class SolicitudForm2(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    #usuario = forms.ChoiceField()
    numero_mascotas = forms.IntegerField(required=True, min_value=1, max_value=5)
    razones = forms.CharField(required=True)