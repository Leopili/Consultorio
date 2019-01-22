from django.contrib import admin

# Register your models here.
from turnos.models import  Turno, Paciente

class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'persona')
    

admin.site.register(Turno, TurnoAdmin)
admin.site.register(Paciente)