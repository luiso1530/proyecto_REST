from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurantes,reservaciones
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    restaurantes = Restaurantes.objects.all()
    context = {'restaurantes':restaurantes}
    #return HttpResponse("hola")
    return render(request,'sistema_de_reservas/index.html',context)
    
def principal(request):
    opciones="Sistema de Reservaciones"
    #return HttpResponse(opciones)
    context = {'opciones':opciones}
    return render(request,'sistema_de_reservas/principal.html',
                              context)

def info_restaurante(request):
    informacion = Restaurantes.objects.all()
    return render(request,'sistema_de_reservas/info_restaurante.html',
                              {'informacion':informacion})
