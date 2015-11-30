from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
 
class Editor(models.Model): 
    
    nombre = models.CharField(max_length=30) 
    domicilio = models.CharField(max_length=50) 
    ciudad = models.CharField(max_length=60) 
    estado = models.CharField(max_length=30) 
    pais = models.CharField(max_length=50) 
    website = models.URLField()

    class Meta():
        ordering = ["nombre"]
        verbose_name_plural = "Editores"

    def __unicode__(self):
        return self.nombre

class Autor(models.Model): 
    nombre = models.CharField(max_length=30) 
    apellidos = models.CharField(max_length=40) 
    email = models.EmailField('e-mail', blank=True) 
    
    class Meta():
        ordering = ["nombre"]
        verbose_name_plural = "Autores"
    
    def __unicode__(self):
        return '%s %s, %s' % (self.nombre, self.apellidos, self.email)
    
    def get_absolute_url(self):
        return reverse('detalles_autor', kwargs={'pk':self.pk})
    
class Libro(models.Model): 
    titulo = models.CharField(max_length=100) 
    autores = models.ManyToManyField(Autor) 
    editor = models.ForeignKey(Editor) 
    fecha_publicacion = models.DateField(blank=True, null=True) 
    portada = models.ImageField(upload_to='portadas') 
    num_paginas = models.IntegerField(blank=True, null=True)

    class Meta():
        ordering = ["titulo"]
        verbose_name_plural = "Libros"

    def __unicode__(self):
        return self.titulo