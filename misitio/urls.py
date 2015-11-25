from django.conf.urls import url, include
from django.contrib import admin

 
urlpatterns = [ 
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
] 
