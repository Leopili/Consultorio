from django.urls import path
from django.contrib.auth.views import login_required
from turnos.views import index_turno, TurnoList, TurnoUpdate, Turno_error, PacienteTurnoList, TurnoCancelar, AgendaList, PacienteUpdate, PacienteDetail
from django.contrib.auth.decorators import login_required

app_name="turnos"
urlpatterns = [
    path('',login_required(index_turno),name="turnos"),
    path('listar/',login_required(TurnoList.as_view()), name='turnos_listar'),
    path('turno/reservar/<int:pk>/',login_required(TurnoUpdate.as_view()), name='turnos_reservar'),
    path('turno/cancelar/<int:pk>/',login_required(TurnoCancelar.as_view()), name='turnos_eliminar'),
    path('mis_turnos/',login_required(PacienteTurnoList.as_view()), name='turno_paciente'),
    path('error/',login_required(Turno_error), name='turnos_error'),
    path('agenda/',login_required(AgendaList.as_view()), name='agenda'),
    path('perfil/',login_required(PacienteUpdate.as_view()), name='actualizar_perfil'),
    path('agenda/<username>',login_required(PacienteDetail), name='paciente_listar'),    
]    