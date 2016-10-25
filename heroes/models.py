from django.db import models

# Create your models here.

class Heroe(models.Model):
	nombre=models.CharField(max_length=100)
	historia=models.TextField()
	poder=models.CharField(max_length=100)
	imagen=models.ImageField(upload_to='images')

	def __str__(self):
		return self.nombre
