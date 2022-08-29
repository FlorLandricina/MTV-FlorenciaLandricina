from http.client import HTTPResponse
from django.db import models
from datetime import date

"""
Consigna: Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.
Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
Se deberán crear como mínimo 3 familiares
Los familiares se deben ver desde la web
"""

class Familiar(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    relacion = models.CharField(max_length=140)
    cantidad_de_hijos = models.IntegerField()
