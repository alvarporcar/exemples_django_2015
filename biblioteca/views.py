from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import Libro


def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')
    
def buscar(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=q)
        return render(request, 'resultados.html', {'libros': libros, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de busqueda.')