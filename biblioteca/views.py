#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import Libro, Editor
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import csv


def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')
    
def buscar(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=q)
        return render(request, 'resultados.html', {'libros': libros, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de busqueda.')
       
class PaginaInicio(TemplateView):
    template_name = "bienvenidos.html"
    
    @method_decorator(login_required) 
    def dispatch(self, *args, **kwargs):
        return super(PaginaInicio, self).dispatch(*args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(PaginaInicio, self).get_context_data(**kwargs) 
        ultimos_libros = Libro.objects.all()[:5]
        num_libros = ultimos_libros.count()
        context['ultimos_libros'] = ultimos_libros
        context['num_libros'] = num_libros
        return context

class ListaEditores(ListView): 
    model = Editor
    context_object_name = 'lista_editores'
    
class DetallesEditor(DetailView): 
    model = Editor
    context_objetct_name = 'editor'
    
    def get_context_data(self, **kwargs):
        # Llama primero a la implementación para traer un contexto 
        context = super(DetallesEditor, self).get_context_data(**kwargs) 
        # Agrega un QuerySet para obtener todos los libros 
        context['lista_libros'] = Libro.objects.all()
        return context    


# Numero de pasajeros problemáticos en el periodo 1995­2005. En una
# aplicacion real estos datos probablemente vendrían de una base de datos 
# o de algún otro tipo de almacenamiento externo.
PASAJEROS_PROBLEMATICOS = [146,184,235,200,226,251,299,273,281,304,203]

def pasajeros_problematicos_csv(request):
    # Crea un objeto HttpResponse con las cabeceras del CVS correctas. 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename = problematicos.csv'
    # Crea el escritor CSV usando un HttpResponse como "archivo."
    writer = csv.writer(response)
    writer.writerow(['Ano', 'Pasajeros problematicos en aerolinea'])
    for (year, num) in zip(range(1995, 2006), PASAJEROS_PROBLEMATICOS):
        writer.writerow([year, num]) 
    return response


