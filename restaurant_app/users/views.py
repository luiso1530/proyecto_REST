from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from .models import usuario,owner

# Create your views here.


def login(request):
    return render(request, 'users/login.html')

def registrar(request):
    return render(request, 'users/registrar.html',)

def newU(request):
    U= usuario(nombre= request.POST.get("nombre",""),user =request.POST.get("usuario",""),contraseña =request.POST.get("password",""))
    U.save()
    return render(request, 'users/login.html')
               
def ingresar(request):
    try:
        selected_choice = usuario.objects.get(nombre = request.POST.get("nombre",""))
    except (KeyError, usuario.DoesNotExist):
        try:
            selected_choice = usuario.objects.get(user = request.POST.get("usuario",""))
        except (KeyError, usuario.DoesNotExist):
            try:
                selected_choice = owner.objects.get(user = request.POST.get("usuario",""))
            except (KeyError, owner.DoesNotExist):
                return render(request, 'users/login.html', {
                    'error_message': "usuario no exite.",
                })
            else:
                return HttpResponseRedirect(reverse('owner:principal', args = (selected_choice.user,)))
        
        else:
            if(selected_choice.contraseña == request.POST.get("password","")):
                return HttpResponseRedirect(reverse('reservas:restaurantes', args = (selected_choice.user,)))
            else:
               return render(request, 'users/login.html', {
                'error_message': "contraseña incorrecta",
            })
    else:
        #return render(request, 'users/login.html', {'error_message': "usuario confirmado",})
        if(selected_choice.contraseña == request.POST.get("password","")):
            return HttpResponseRedirect(reverse('reservas:restaurantes', args = (selected_choice.user,)))
        else:
           return render(request, 'users/login.html', {
            'error_message': "contraseña incorrecta",
        })
