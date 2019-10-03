from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index_mascota(request):
    #return HttpResponse("Index")
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_mascota')
    else:
        form = MascotaForm()
    return render(request, 'mascota/form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/list.html', contexto)