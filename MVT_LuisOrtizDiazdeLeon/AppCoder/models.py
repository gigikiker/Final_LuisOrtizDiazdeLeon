from django.db import models
from datetime import datetime 


class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    indicador=models.IntegerField()
    
class Entrenadores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    badge=models.IntegerField(default=0000)
    indicador=models.IntegerField(default=0000)

class Pokemon(models.Model):
    nombre=models.CharField(max_length=40)
    tipo=models.CharField(max_length=40)
    sexo=models.CharField(max_length=40)
    badge=models.IntegerField(default=0000)
    fecha_de_captura=models.DateField()
    en_equipo=models.BooleanField()
    