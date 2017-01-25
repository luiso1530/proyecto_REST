from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurantes,reservaciones
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    restaurantes = Restaurantes.objects.all()
    context = {'restaurantes':restaurantes}
    return render(request,'sistema_de_reservas/index.html',
                              context)
    
def principal(request,pk):
    opciones = Restaurantes.objects.get(pk=pk)
    return render(request,'sistema_de_reservas/principal.html',
                              {'opciones':opciones})

def info_restaurante(request,pk):
    informacion = Restaurantes.objects.get(pk=pk)
    return render(request,'sistema_de_reservas/info_restaurante.html',
                              {'informacion':informacion})

def mis_reservas(request):
    reservas = reservaciones.objects.all()
    return render(request,'sistema_de_reservas/mis_reservas.html',
                              {'reservas':reservas})

def hora_reserva(request):
    confirmadas = reservaciones.objects.all()
    return render(request,'sistema_de_reservas/mis_reservas.html',
                              {'Reservaciones':confirmadas})

def dia_reserva(request):
    dia_personas = reservaciones.objects.all()
    return render(request,'sistema_de_reservas/dia_reserva.html',
                              {'Dia_personas':dia_personas})
