from django.shortcuts import render
from django.http import HttpResponse
from sistemareservas.models import Restaurantes,reservaciones
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    restaurantes = Restaurantes.objects.all()
    context = {'restaurantes':restaurantes}
    return render(request,'sistemareservas/index.html',
                              context)
    
def principal(request,pk):
    opciones = Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/principal.html',
                              {'opciones':opciones})

def info_restaurante(request,pk):
    informacion = Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/info_restaurante.html',
                              {'informacion':informacion})

def mis_reservas(request):
    reservas = reservaciones.objects.all()
    return render(request,'sistemareservas/mis_reservas.html',
                              {'reservas':reservas})

def hora_reserva(request):
    confirmadas = reservaciones.objects.all()
    return render(request,'sistemareservas/mis_reservas.html',
                              {'Reservaciones':confirmadas})

def dia_reserva(request):
    dia_personas = reservaciones.objects.all()
    return render(request,'sistemareservas/dia_reserva.html',
                              {'Dia_personas':dia_personas})
    
