from django import forms
from turnos.models import Turno, Paciente

class TurnoForm(forms.ModelForm):
	
	class Meta:
		model = Turno
		fields = [
			'fecha',					
		]
		labels = {			
			'fecha': 'Fecha: ',		
			
		}
		
		
		widgets = {
		        'fecha': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
		    }


		
class CancelarTurnoForm(forms.ModelForm):
	
	class Meta:
		model = Turno
		fields = [
			'fecha',					
		]
		labels = {			
			'fecha': 'Fecha: ',		
			
		}
	

