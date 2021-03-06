from django import forms
from apps.mascota.models import Mascota, User, Vacuna
from django.contrib.auth.models import User

class MascotaForm(forms.ModelForm):

    #ForeignKey = forms.ModelChoiceField(queryset=ChildOfMany.objects.all())
    #OneToOneField = forms.ModelChoiceField(queryset=ChildOfOne.objects.all())
    #ManyToManyField = forms.ModelMultipleChoiceField(queryset=Vacuna.objects.all(), required=False)
    #CheckboxSelectMultiple = forms.CharField(max_length=10, widget=forms.CheckboxSelectMultiple())
    #CheckboxSelectMultiple = forms.CharField(max_length=10, widget=forms.CheckboxSelectMultiple(choices=TITLE_CHOICES))

    class Meta:
        model = Mascota
        #TEST_CHOICES = [[x.id, x.nombre] for x in Vacuna.objects.all()]
        #queryset = Vacuna.objects.all()
        #vacunas = forms.ModelMultipleChoiceField(queryset=Vacuna.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)

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
            #'vacuna': vacunas,
        }

class VacunaForm(forms.ModelForm):
    
    class Meta:
        model = Vacuna

        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }