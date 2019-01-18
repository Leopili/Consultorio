from django.db import models
from django.contrib.auth.models import User



class Turno(models.Model):
	persona = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField("Fecha y Hora")

	class Meta:
		verbose_name_plural = "Turnos"

	
	
	def __str__(self):
		return "{}".format(self.fecha)

