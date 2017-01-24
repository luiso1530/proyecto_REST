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
    
def principal(request):
    opciones="Sistema de Reservaciones"
    #return HttpResponse(opciones)
    context = {'opciones':opciones}
    return render(request,'sistemareservas/principal.html',
                              context)

def info_restaurante(request):
    informacion = Restaurantes.objects.all()
    return render(request,'sistemareservas/info_restaurante.html',
                              {'informacion':informacion})
