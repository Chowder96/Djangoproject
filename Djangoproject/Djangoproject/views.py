from django.http import HttpResponse
import datetime as dt

def saludo(request):
    return HttpResponse("Hola Django- Coder")

def fecha(request):
    fecha_actual = dt.datetime.now()
    return HttpResponse(f"Hoy es: {fecha_actual}")