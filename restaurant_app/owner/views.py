from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from users.models import usuario,owner
from sistema_de_reservas.models import Restaurantes, reservaciones
# Create your views here.

def principal(request, own):
    latest_question_list = owner.objects.get(user = own)
    restaurante = Restaurantes.objects.get(pk = 1)#context.restaurante)
    context = {
        'usuario': latest_question_list,
        'restaurante' : restaurante,
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