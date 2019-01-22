from django.db import models
from django.contrib.auth.models import User



class Paciente(models.Model):
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	dni = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	domicilio = models.CharField(max_length=50)
	obra_social = models.CharField(max_length=50)

	class Meta:
		verbose_name = "paciente"
		verbose_name_plural = "pacientes"
		ordering = ['nombre', 'apellido']    


	def __str__(self):
		return "{} ¨{}".format(self.nombre, self.apellido)


class Turno(models.Model):
	persona = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField("Fecha y Hora")

	class Meta:
		verbose_name_plural = "Turnos"

	
	
	def __str__(self):
		return "{}".format(self.fecha)