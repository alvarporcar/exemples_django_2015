from django.conf.urls import url, include
from django.contrib import admin
from misitio.views import hola, fecha_actual, horas_adelante, mostrar_navegador, atributos_meta, atributos_meta_template
from biblioteca import views
from contactos.views import contactos

 
urlpatterns = [ 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', hola), 
    url(r'^fecha/$', fecha_actual), 
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante), 
    url(r'^navegador/', mostrar_navegador),
    url(r'^atributos_meta/', atributos_meta),
    url(r'^atributos_meta_template/', atributos_meta_template),
    url(r'^formulario_buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^contactos/$', contactos),
] 
