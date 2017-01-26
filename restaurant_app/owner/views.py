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
