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

def hora_reserva(request,pk):
    rest=Restaurantes.objects.get(pk=pk)
    D = reservaciones(cantidad_personas= request.POST.get("cantidad",""),dia =request.POST.get("fecha",""),hora=request.POST.get("hora",""),restaurantes=rest.nombre)
    D.save()
    confirmadas = reservaciones.objects.filter(cantidad_personas=D.cantidad_personas)
    return render(request,'sistema_de_reservas/hora_reserva.html',
                              {'Confirmadas':confirmadas,'rest':rest})

def dia_reserva(request,pk):
    r=Restaurantes.objects.get(pk=pk)
    return render(request,'sistema_de_reservas/dia_reserva.html',
                  {'rest':r})
