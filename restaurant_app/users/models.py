from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=20)
    user= models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)

class owner(models.Model):
    nombre = models.CharField(max_length=20)
    user= models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    restaurante = models.IntegerField(default=0) 
