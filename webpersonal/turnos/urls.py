from django.urls import path
from django.contrib.auth.views import login_required
from turnos.views import index_turno, TurnoList, TurnoUpdate, Turno_error, PacienteTurnoList, TurnoCancelar

app_name="turnos"
urlpatterns = [
    path('',index_turno,name="turnos"),
    path('listar/',TurnoList.as_view(), name='turnos_listar'),
    path('turno/reservar/<int:pk>/',TurnoUpdate.as_view(), name='turnos_reservar'),
    path('turno/cancelar/<int:pk>/',TurnoCancelar.as_view(), name='turnos_eliminar'),
    path('mis_turnos/',PacienteTurnoList.as_view(), name='turno_paciente'),
    path('error/',Turno_error, name='turnos_error'),    
    

    
]    