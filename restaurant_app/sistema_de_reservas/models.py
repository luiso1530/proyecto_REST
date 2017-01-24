from django.db import models

# Create your models here.

class Restaurantes(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    numero_tel = models.IntegerField()

    def __str__(self):
        return self.asunto
    
class reservaciones(models.Model):
    
    Opciones_Horas = (
        ('1:00 pm', 'una'),
        ('2:00 pm', 'dos'),
        ('2:00 pm', 'tres'),
    )
    cliente = models.CharField(max_length=20)
    #fecha = models.ForeignKey()#aqui poner referencia a un modelo de calendario
    cantidad_personas = models.IntegerField()
    hora = models.CharField(max_length=1, choices=Opciones_Horas)