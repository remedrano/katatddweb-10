# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from servicio.models import Servicio
from datetime import datetime


# Create your models here.

class Independiente(models.Model):
    servicio = models.ForeignKey(Servicio)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    foto = models.CharField(max_length=200)
    experiencia = models.IntegerField()
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'independiente'
        verbose_name_plural = 'independientes'
        db_table = 'independiente'

    def __str__(self):
        return '%s' % (self.nombre)


class Comentario(models.Model):
    comentario = models.CharField(max_length=500, default="")
    independiente = models.ForeignKey(Independiente, null=True )
    fecha = models.DateTimeField(null=True, default=datetime.now(), blank=True)
    correo = models.CharField(max_length=100, default="" )

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
        db_table = 'comentario'