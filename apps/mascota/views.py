from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
#listas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse_lazy VERSION VIEJA DE DJANGO
from django.urls import reverse_lazy
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota, Vacuna
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from apps.mascota.serializer import MascotaSerializer, VacunaSerializer

# Create your views here.

# Serializado para la API: clase
class ListMascota(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        mascotas_json = MascotaSerializer(mascotas, many=True)
        return Response (mascotas_json.data)

    def post(self, request):
        mascotas_json = MascotaSerializer(data=request.data) #UnMarshall
        if mascotas_json.is_valid():
            mascotas_json.save()
            return Response(mascotas_json.data, status=201)
        else:
            return Response(mascotas_json.errors, status=400)

class ListVacuna(APIView):
    def get(self, request):
        vacunas = Vacuna.objects.all()
        vacunas_json = VacunaSerializer(vacunas, many=True)
        return Response (vacunas_json.data)

    def post(self, request):
        vacunas_json = VacunaSerializer(data=request.data) #UnMarshall
        if vacunas_json.is_valid():
            vacunas_json.save()
            return Response(vacunas_json.data, status=201)
        else:
            return Response(vacunas_json.errors, status=400)

###################

class DetailMascota(APIView):
    def get_object(self, pk):
        try:
            #mascota = Mascota.objects.get(pk=pk)
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mascota = self.get_object(pk)
        mascota_json = MascotaSerializer(mascota)
        return Response (mascota_json.data)

    def put(self, request, pk):
        mascota = self.get_object(pk)
        mascota_json = MascotaSerializer(mascota, data=request.data)
        if mascota_json.is_valid():
            mascota_json.save()
            return Response(mascota_json.data)
        return Response(mascota_json.errors, status=400)
    
    def delete(self, request, pk):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=204)


class DetailVacuna(APIView):
    def get_object(self, pk):
        try:
            return Vacuna.objects.get(pk=pk)
        except Vacuna.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vacuna = self.get_object(pk)
        vacuna_json = VacunaSerializer(vacuna)
        return Response (vacuna_json.data)

    def put(self, request, pk):
        vacuna = self.get_object(pk)
        vacuna_json = VacunaSerializer(vacuna, data=request.data)
        if vacuna_json.is_valid():
            vacuna_json.save()
            return Response(vacuna_json.data)
        return Response(vacuna_json.errors, status=400)
    
    def delete(self, request, pk):
        vacuna = self.get_object(pk)
        vacuna.delete()
        return Response(status=204)


def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all())
    return HttpResponse(lista, content_type='application/json')

def index_mascota(request):
    #return HttpResponse("Index")
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('index_mascota')
        return redirect('mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(request, 'mascota/delete.html', {'mascota':mascota})

#listas basadas en clases
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/list.html'
    paginate_by = 5

class MascotaCreate(SuccessMessageMixin ,CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/form.html'
    #success_url = reverse_lazy('mascota:mascota_listar')
    success_url = reverse_lazy('mascota_listar')
    #success_message = "%(name)s was created successfully"
    success_message = "%(nombre)s ha sido registrado con éxito!"
    #messages.success(request, 'La mascota fue agregada!')

    """
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
        cleaned_data,
        calculated_field=self.object.calculated_field,
    )
    """

class MascotaUpdate(SuccessMessageMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/form.html'
    success_url = reverse_lazy('mascota_listar')
    success_message = "%(nombre)s ha sido modificado con éxito!"

class MascotaDelete(SuccessMessageMixin, DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/delete.html'
    success_url = reverse_lazy('mascota_listar')
    success_message = "%(nombre)s ha sido eliminado con éxito!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(MascotaDelete, self).delete(request, *args, **kwargs)

        #messages.success(self.request, self.success_message)
        #return super(MascotaDelete, self).delete(request, *args, **kwargs)