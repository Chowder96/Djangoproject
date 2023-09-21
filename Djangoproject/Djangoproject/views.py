from django.http import HttpResponse
import datetime as dt
from django.template import Template, Context

def saludo(request):
    return HttpResponse("<h1>Hola Django- Coder</h1>")

def fecha(request):
    fecha_actual = dt.datetime.now()
    return HttpResponse(f"Hoy es: {fecha_actual}")

def diaDeHoy(request):
    fecha_actual = dt.datetime.now()
    return HttpResponse(f"Hoy es el dia numero <b>{fecha_actual.day}</b> del mes numero <b>{fecha_actual.month}</b> del año <b>{fecha_actual.year}</b>")

def mi_nombre(request, nombre):
    texto = f"Hola, mi nombre es: <br> <br> {nombre.capitalize()}"
    return HttpResponse(texto)

def pagina(request):
    ahora = dt.datetime.now()
    lista_numeros = [1, 3, 5 ,7, 9]
    name = 'Pepe'

    diccionario = {'ahora': ahora, 'lista_numeros': lista_numeros, 'name': name}

    miHtml = open(r'C:\Djangoproject\Djangoproject\Djangoproject\Plantillas\template1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()

    context1 = Context(diccionario)
    return HttpResponse(plantilla.render(context1))