from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from users.models import usuario,owner
from sistema_de_reservas.models import Restaurantes, reservaciones
import time
# Create your views here.

def principal(request, own):
    latest_question_list = owner.objects.get(user = own)
    restaurante = Restaurantes.objects.get(pk = latest_question_list.restaurante)
    minimo= time.strftime("%Y-%m-%d")
    context = {
        'usuario': latest_question_list,
        'restaurante' : restaurante,
        'fecmin': minimo,
    }
    return render(request, 'owner/principal.html', context)
    #template = loader.get_template('owner/principal.html')
    #return HttpResponse(template.render(context,restaurante, request))

def peticiones(request, own):
    o = owner.objects.get(user = own)
    rest = Restaurantes.objects.get(pk = o.restaurante)
    peticiones = reservaciones.objects.filter(restaurantes = rest.nombre)
    output = peticiones.order_by('-dia')
    return render(request, 'owner/peticiones.html', {'peticion': output,'own':o})

def solicitudes(request,own,pk):
    o = owner.objects.get(user = own)
    peticiones = reservaciones.objects.get(pk=pk)
    return render(request, 'owner/peticion.html', {'peticion': peticiones,'own':o})

def solicitud_fecha(request,own):
    o = owner.objects.get(user = own)
    rest = Restaurantes.objects.get(pk = o.restaurante)
    peticiones = reservaciones.objects.filter(restaurantes = rest.nombre)
    fecha = request.POST.get("fecha","")
    minimo= time.strftime("%Y/%m/%d")
    output = peticiones.filter(dia = fecha).order_by('-hora')
    return render(request, 'owner/peticiones.html', {'peticion': output,'own':o})
