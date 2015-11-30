#coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin
from biblioteca.views import PaginaInicio, ListaEditores, DetallesEditor
from misitio.views import MiVista
from django.views.generic.base import TemplateView
from biblioteca.forms import CrearAutor, ActualizarAutor, BorrarAutor
 
urlpatterns = [ 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', 'misitio.views.hola'), 
    url(r'^fecha/$', 'misitio.views.fecha_actual'), 
    url(r'^fecha/mas/(\d{1,2})/$', 'misitio.views.horas_adelante'), 
    url(r'^navegador/', 'misitio.views.mostrar_navegador'),
    url(r'^atributos_meta/', 'misitio.views.atributos_meta'),
    url(r'^atributos_meta_template/', 'misitio.views.atributos_meta_template'),
    url(r'^formulario_buscar/$', 'biblioteca.views.formulario_buscar'),
    url(r'^buscar/$', 'biblioteca.views.buscar'),
    url(r'^contactos/$', 'contactos.views.contactos'),
    url(r'^ws_temps/$', 'misitio.views.ws_temps'),
    url(r'^ws_rss/$', 'misitio.views.ws_rss'),
    url(r'^hola/$', MiVista.as_view(), name='mi_vista'),
    url(r'^benvinguda/$', PaginaInicio.as_view(), name='benvinguts'),
    url(r'^acerca/', TemplateView.as_view(template_name="acerca_de.html")),
    url(r'^editores/$', ListaEditores.as_view(template_name="editor_list.html"), name ='lista_editores'),
    url(r'^detalles/editor/(?P<pk>[0-9]+)/$', DetallesEditor.as_view(template_name="editor_detail.html"), name='detalles_editor' ),
    url(r'^autor/agregar/$', CrearAutor.as_view(template_name='autor_form.html'), name='agregar_autor'), 
    url(r'^autor/(?P<pk>[0-9]+)/$', ActualizarAutor.as_view(template_name='autor_form.html'), name='actualizar_datos'), 
    url(r'^autor/(?P<pk>[0-9]+)/borrar/$', BorrarAutor.as_view(template_name='autor_confirm_delete.html'), name='borrar_autor'),
    url(r'^problematicos/$', 'biblioteca.views.pasajeros_problematicos_csv'),

]
