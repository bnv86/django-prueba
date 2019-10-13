from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, UserChangeForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserEditForm(forms.ModelForm): #UserChangeForm

    class Meta: #class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'first_name','last_name','email']

"""
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }

"""

"""
class UserForm(forms.ModelForm):            
        middle_name = forms.CharField(required=False, max_length=50)
        password = forms.CharField(widget=forms.PasswordInput())
        about_company = forms.CharField(required=False, max_length=50)

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': '{}'.format(field).replace("_", ' ').capitalize(),

                })

            self.fields['email'].widget.attrs['placeholder'] = 'abc@xyz.com'
            self.fields['email'].required = True
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['password'].required = True

            if self.instance.pk:
                self.fields['username'].required = False
                self.fields['username'].widget.attrs['readonly'] = True
                self.fields['email'].required = False
                self.fields['email'].widget.attrs['readonly'] = True
                self.fields['password'].widget.attrs['readonly'] = True
                self.fields['password'].required = False

        def save(self, *args, **kwargs):
            self.date_joined = date.today()
            super(UserForm, self).save(*args, **kwargs)
            return self

        class Meta:
            model = User
            fields = '__all__'
            exclude = ('date_joined',)
"""


"""
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
"""

"""
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
"""

"""
class UpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }
"""