from django.db import models

# Create your models here.

class Restaurantes(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    numero_tel = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class reservaciones(models.Model):
    cliente = models.CharField(max_length=20)
    restaurantes = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)#aqui poner referencia a un modelo de calendario
    cantidad_personas = models.CharField(max_length=20)
    dia = models.DateField()

    def __str__(self):
        return self.cantidad_personas
    def __str__(self):
        return self.cliente
    def __str__(self):
        return self.dia
    





