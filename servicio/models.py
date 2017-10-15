# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        db_table='servicio'

    def __str__(self):
        return '%s' % (self.nombre)