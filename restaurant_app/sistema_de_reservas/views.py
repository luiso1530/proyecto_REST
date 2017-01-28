from django.shortcuts import render
from django.http import HttpResponse
from users.models import usuario,owner
from sistema_de_reservas.models import Restaurantes,reservaciones
from django.shortcuts import render_to_response

# Create your views here.

def index(request, user):
    use = usuario.objects.get(user=user)
    restaurantes = Restaurantes.objects.all()
    context = {'restaurantes':restaurantes, 'usuario':use}
    return render(request,'sistemareservas/index.html',
                              context)
    
def principal(request,user,pk):
    use = usuario.objects.get(user=user)
    opciones = Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/principal.html',
                              {'opciones':opciones, 'usuario':use})

def info_restaurante(request,pk):
    informacion = Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/info_restaurante.html',
                              {'informacion':informacion})

def mis_reservas(request):
    reservas = reservaciones.objects.all()
    return render(request,'sistemareservas/mis_reservas.html',
                              {'reservas':reservas})

def hora_reserva(request,user,pk):
    use = usuario.objects.get(user=user)
    rest=Restaurantes.objects.get(pk=pk)
    D = reservaciones(cliente= use.nombre,
                      cantidad_personas= request.POST.get("cantidad",""),
                      dia =request.POST.get("fecha",""),
                      restaurantes=rest.nombre)
    D.save()
    confirmadas = reservaciones.objects.filter(cantidad_personas=D.cantidad_personas)
    return render(request,'sistemareservas/hora_reserva.html',
                              {'Confirmadas':confirmadas,'usuario':use,'D':D})

def dia_reserva(request,user,pk):
    use = usuario.objects.get(user=user)
    r=Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/dia_reserva.html',
                  {'rest':r, 'usuario':use})

def final(request,ident,pk):
    r=usuario.objects.get(pk=pk)
    reserva=reservaciones.objects.get(pk=ident)
    D=request.POST.get("hora","")
    reserva.hora=D
    reserva.save()
    return render(request,'sistemareservas/final.html',{'D':D, 'rest':r})
    
