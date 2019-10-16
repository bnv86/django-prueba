from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
from apps.usuario.models import User
from django.urls import reverse_lazy
from django.core import serializers

# Create your views here.

def listadoPersona(request):
    lista = serializers.serialize('json', Persona.objects.all())
    return HttpResponse(lista, content_type='application/json')

def listadoSolicitud(request):
    lista = serializers.serialize('json', Solicitud.objects.all())
    return HttpResponse(lista, content_type='application/json')

def index_adopcion(request):
    return HttpResponse("Adopciones")

class SolicitudList(ListView):
    #fields = '__all__'
    model = Solicitud
    template_name = 'adopcion/list.html'
    paginate_by = 5

class SolicitudCreate(SuccessMessageMixin, CreateView):
    fields = '__all__'
    model = Solicitud
    #form_class1 = SolicitudForm
    #form_class2 = PersonaForm
    template_name = 'adopcion/form_old.html'
    success_url = reverse_lazy('solicitud_listar')
    success_message = "La solicitud ha sido generada con éxito!"

    """
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
    """
    

class SolicitudUpdate(SuccessMessageMixin, UpdateView):
    fields = '__all__'
    model = Solicitud
    model2 = Persona
    #form_class = SolicitudForm
    #form_class2 = PersonaForm
    template_name = 'adopcion/form_old.html'
    success_url = reverse_lazy('solicitud_listar')
    success_message = "La solicitud ha sido modificada con éxito!"

    """
    #sobreescribir los metodos de las vistas basadas en clases (get_context_data)
    #ESTO NO ESTÁ FUNCIONANDO EN EL GET DEBIDO AL USO DE LOS 2 FORMULARIOS
    def get_context_data(self, **kwargs):
        #self.object = self.get_object
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model1.objects.get(id=pk)
        persona = self.model2.objects.get(id=solicitud.persona_id)
        if 'form1' not in context:
            context['form1'] = self.form_class1()
        if 'form2' not in context:
            context['form2'] = self.form_class2(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_solicitud = kwargs['pk']
        solicitud = self.model1.objects.get(id=id_solicitud)
        persona = self.model2.objects.get(id=solicitud.persona_id)
        form1 = self.form_class1(request.POST, instance=solicitud)
        form2 = self.form_class2(request.POST, instance=persona)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
"""

class SolicitudDelete(SuccessMessageMixin, DeleteView):
    model = Solicitud
    template_name = 'adopcion/delete.html'
    success_url = reverse_lazy('solicitud_listar')
    success_message = "La solicitud ha sido eliminada con éxito!"

    #con esto se emite el success_message
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(SolicitudDelete, self).delete(request, *args, **kwargs)


"""
class RecipeUpdateView(UpdateView):
    template_name = 'adopcion/form.html'
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        self.success_url = '/account/dashboard/'
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = RecipeForm(self.request.POST, instance=self.object)
            context['ingredient_form'] = IngredientFormSet(self.request.POST, instance=self.object)
            context['instruction_form'] = InstructionFormSet(self.request.POST, instance=self.object)
        else:
            context['form'] = RecipeForm(instance=self.object)
            context['ingredient_form'] = IngredientFormSet(instance=self.object)
            context['instruction_form'] = InstructionFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))
"""
