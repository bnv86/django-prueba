import json
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.core import serializers
from django.http import HttpResponse
from apps.usuario.serializer import UserSerializer

# Create your views here.

def listado(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'email', 'first_name', 'last_name'])
    return HttpResponse(lista, content_type='application/json')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm #UserCreationForm
    success_url = reverse_lazy('mascota_listar')

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')