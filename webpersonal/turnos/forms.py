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
	
class PacienteForm(forms.ModelForm):
	
	class Meta:
		model = Paciente
		fields = [
			'nombre','apellido','dni','telefono','domicilio','obra_social',					
		]
		labels = {			
			'nombre': 'Nombre: ',
			'apellido': 'Apellido: ',
			'dni': 'DNI: ',
			'telefono': 'Teléfono: ',
			'domicilio': 'Domicilio: ',
			'obra_social': 'Obra Social: ',	
			
		}

		widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'obra_social': forms.TextInput(attrs={'class':'form-control'}),
        }
