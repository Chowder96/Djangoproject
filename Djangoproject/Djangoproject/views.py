from django.http import HttpResponse
import datetime as dt

def saludo(request):
    return HttpResponse("<h1>Hola Django- Coder</h1>")

def fecha(request):
    fecha_actual = dt.datetime.now()
    return HttpResponse(f"Hoy es: {fecha_actual}")

def diaDeHoy(request):
    fecha_actual = dt.datetime.now()
    return HttpResponse(f"Hoy es el dia numero <b>{fecha_actual.day}</b> del mes numero <b>{fecha_actual.month}</b> del año <b>{fecha_actual.year}</b>")
