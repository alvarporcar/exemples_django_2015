from django.http import HttpResponse, Http404
from django.shortcuts import render 

import datetime
 
def hola(request): 
    return HttpResponse("Hola Mundo") 

def fecha_actual(request): 
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora}) 

def horas_adelante(request, offset): 
    try: 
        offset = int(offset) 
    except ValueError: 
        raise Http404()  
    dt= datetime.datetime.now()+datetime.timedelta(hours=offset)        
    html = "<html><body><h1>En %s hora(s), seran:</h1><h2>%s</h2></body></html>" % (offset, dt) 
    return HttpResponse(html)  


def mostrar_navegador(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown') 
    return HttpResponse("Tu navegador es %s" % ua)
    
def atributos_meta(request): 
    valor = request.META.items() 
    valor.sort()
    html = []
    for k, v in valor: 
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
def atributos_meta_template(request):
    return render(request, 'atributos_meta.html', {'atributos': request.META.items()})