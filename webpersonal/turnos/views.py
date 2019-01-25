from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from turnos.models import Turno, Paciente
from turnos.forms import TurnoForm, CancelarTurnoForm, PacienteForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User


def index_turno(request):
	return render(request, "turnos/turnos.html")
	
class TurnoList(ListView):
	model = Turno
	template_name = 'turnos/turnos_list.html'
	queryset = model.objects.filter(persona__isnull=True)

class AgendaList(ListView):
	model = Turno
	template_name = 'turnos/agenda.html'
	

class TurnoUpdate(UpdateView):
	model = Turno	
	template_name = 'turnos/turnos_form.html'
	form_class = TurnoForm	
	success_url = reverse_lazy('turnos:turnos_listar')


	def get_context_data(self, **kwargs):
	    context = super(TurnoUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    turno = self.model.objects.get(id=pk)	    
	    if 'form' not in context:
	    	context['form'] = self.form_class()	    
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_turno = kwargs['pk']
		turno = self.model.objects.get(id=id_turno)		
		form = self.form_class(request.POST, instance=turno)

		if form.is_valid():
			try:						 
				form.save(commit=False)
				turno.persona = request.user						
				form.save()
				return HttpResponseRedirect(self.get_success_url())
			except IntegrityError:
				return redirect("turnos:turnos_error")



def Turno_error(request):
	return render(request, "turnos/turnos_error.html")		


class PacienteTurnoList(ListView):
	model = Turno
	template_name = 'turnos/turno_paciente.html'

	def get_queryset(self):
		return Turno.objects.filter(persona=self.request.user)

class TurnoCancelar(UpdateView):
	model = Turno	
	template_name = 'turnos/turnos_form2.html'
	form_class = CancelarTurnoForm	
	success_url = reverse_lazy('turnos:turnos_listar')


	def get_context_data(self, **kwargs):
	    context = super(TurnoCancelar, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    turno = self.model.objects.get(id=pk)	    
	    if 'form' not in context:
	    	context['form'] = self.form_class()	    
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_turno = kwargs['pk']
		turno = self.model.objects.get(id=id_turno)		
		form = self.form_class(request.POST, instance=turno)

		if form.is_valid():
			form.save(commit=False)
			turno.persona = None					
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

def PacienteDetail(request, username):
    paciente = get_object_or_404(Paciente, user__username=username)
    context = {'paciente': paciente}
    return render(request, 'turnos/paciente_detail.html' , context )

	

class PacienteUpdate(UpdateView):
	model = Paciente
	form_class = PacienteForm	
	success_url = reverse_lazy('inicio')
	template_name = 'turnos/paciente_form.html'
	

	def get_object(self):
		paciente, created = Paciente.objects.get_or_create(user=self.request.user)	
		return paciente
	


	