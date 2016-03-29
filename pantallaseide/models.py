# -*- coding: utf-8 -*-
from django.db import models

class Pantalla(models.Model):
    nombre = models.CharField('Nombre',max_length=255,)
    def __unicode__(self):
        return self.nombre
    def get_carrousel_activo(self):
        return self.carrusel_set.filter(activo=True)[0]
    
class Carrusel(models.Model):
    nombre = models.CharField('Nombre',max_length=255,)
    pantalla = models.ForeignKey(Pantalla)
    activo = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nombre
    def get_imagenes_orden(self):
        return self.imagen_set.all().order_by('orden')
    
class Imagen(models.Model):
    nombre = models.CharField('Nombre',max_length=255,)
    imagen = models.ImageField(upload_to="imgenes/", null=True, blank=True)
    carrusel = models.ForeignKey(Carrusel)
    orden = models.DecimalField(max_digits=2,decimal_places=0,default=01)
    def __unicode__(self):
        return self.nombre
    
