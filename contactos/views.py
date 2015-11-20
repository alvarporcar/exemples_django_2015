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
            send_mail(
                    cd['asunto'],
                    cd['mensaje'],
                    cd.get('alvar.porcar@gmail.com'),['email'], )
            return HttpResponseRedirect('/contactos/gracias/') 
    else:
        form = FormularioContactos()
    return render(request,'formulario_contactos.html', {'form': form})