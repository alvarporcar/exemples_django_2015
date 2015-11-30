from django.http import HttpResponse, Http404
from django.shortcuts import render 
from suds.client import Client
from django.views.generic import View

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

 
def ws_temps(request):
    url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
    client = Client(url)
    weather =  client.service.GetWeather('Valencia', 'Spain')
    return HttpResponse(weather)

def ws_rss(request):
    url = 'http://www.webservicex.net/RssToHTML.asmx?WSDL'
    client = Client(url)
    resposta =  client.service.GetHTML('http://cabanes.es/es/rss.xml')
    return HttpResponse(resposta)

class MiVista(View):
    def get(self, request, *args, **kwargs): 
        return HttpResponse('Hola Mundo')
