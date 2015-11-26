from django import template

register = template.Library

@register.filter(name='cortar')
def cortar(value,arg):
    # Borra todos los valores de los argumentos que concuerdan con la cadena dada
    return value.replace(arg,"")

@register.filter(name='minusculas')
def minusculas(valor):
    # Convierte una cadena a minusculas
    return valor.lower()
