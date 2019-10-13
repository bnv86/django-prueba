import json
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.core import serializers
from django.http import HttpResponse
from apps.usuario.serializer import UserSerializer
#from django.contrib.auth.signals import user_logged_out
#from django.dispatch import receiver

# Create your views here.

# Serializado para la API
def listado(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'email', 'first_name', 'last_name'])
    return HttpResponse(lista, content_type='application/json')

class RegistroUsuario(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm #UserCreationForm
    success_url = reverse_lazy('login')
    # en algun momento tengo que cambiar esto, para que primero envie un mail de confirmacion como en password_reset
    success_message = "%(username)s ha sido registrado con éxito!"

#implementar en urls globales y en logout.html
class LogoutUsuario(SuccessMessageMixin, LogoutView):
    model = User
    #form_class = MascotaForm
    #template_name = 'mascota/delete.html'
    success_url = reverse_lazy('login')
    success_message = "%(username)s ha cerrado sesión!"


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')