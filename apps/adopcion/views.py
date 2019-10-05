from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
from django.urls import reverse_lazy

# Create your views here.

def index_adopcion(request):
    return HttpResponse("Adopciones")

class SolicitudList(ListView):
    #fields = '__all__'
    model = Solicitud
    template_name = 'adopcion/list.html'

class SolicitudCreate(CreateView):
    fields = '__all__'
    model = Solicitud
    form_class1 = SolicitudForm
    form_class2 = PersonaForm
    template_name = 'adopcion/form.html'
    success_url = reverse_lazy('solicitud_listar')

    #sobreescribir los metodos de las vistas basadas en clases (get_context_data)
    def get_context_data(self, **kwargs):
        contexto = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form1' not in contexto:
            contexto['form1'] = self.form_class1(self.request.GET)
        if 'form2' not in contexto:
            contexto['form2'] = self.form_class2(self.request.GET)
        return contexto

    def post_data(self, request, *args, **kwargs):
        self.object = self.get_object
        form1 = self.form_class1(request.POST)
        form2 = self.form_class2(request.POST)
        if form1.is_valid() and form2.is_valid():
            solicitud = form1.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form1=form1, form2=form2))

class SolicitudUpdate(UpdateView):
    fields = '__all__'
    model1 = Solicitud
    model2 = Persona
    form_class1 = SolicitudForm
    form_class2 = PersonaForm
    template_name = 'adopcion/form.html'
    #success_url = reverse_lazy('solicitud_listar')

    #sobreescribir los metodos de las vistas basadas en clases (get_context_data)
    def get_context_data(self, **kwargs):
        #self.object = self.get_object
        contexto = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model1.objects.get(id=pk)
        persona = self.model2.objects.get(id=solicitud.persona_id)
        if 'form1' not in contexto:
            contexto['form1'] = self.form_class1()
        if 'form2' not in contexto:
            contexto['form2'] = self.form_class2(instance=persona)
        contexto['id'] = pk
        return contexto