# -*- coding: utf-8 -*-

from django.shortcuts import render
from contactos.forms import FormularioContactos
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data 
            assumpte = cd['asunto']
            missatge = cd['mensaje']
            destinatari = cd['email']
            print "send_mail("+assumpte+","+missatge+","+"alvar.porcar@gmail.com"+",["+destinatari+"],"+"fail_silently=False)"
            send_mail(assumpte,missatge,'alvar.porcar@gmail.com',['destinatari'],fail_silently=False)
            
            return HttpResponseRedirect('/contactos/gracias/') 
    else:
        form = FormularioContactos()
    return render(request,'formulario_contactos.html', {'form': form})