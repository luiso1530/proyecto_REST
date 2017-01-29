from django.shortcuts import render
from django.http import HttpResponse
from users.models import usuario,owner
from sistema_de_reservas.models import Restaurantes,reservaciones
from django.shortcuts import render_to_response
import datetime

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

def mis_reservas(request, user , pk):
    opciones = Restaurantes.objects.get(pk=pk)
    use = usuario.objects.get(user=user)
    reservas = reservaciones.objects.filter(cliente = use.user, restaurantes =opciones.nombre)
    rest = reservas.order_by('-dia','-hora')
    return render(request,'sistemareservas/mis_reservas.html',
                              {'opciones':opciones , 'reservas':rest})

def reserva(request, user, pk , ident):
    use = usuario.objects.get(user=user)
    rest=Restaurantes.objects.get(pk=pk)
    reservas = reservaciones.objects.get(pk=ident)
    context={'usuario':use,'restaurante':rest,'reserva':reservas}
    return render(request,'sistemareservas/reserva.html',
                              context)

def hora_reserva(request,user,pk):
    use = usuario.objects.get(user=user)
    rest=Restaurantes.objects.get(pk=pk)
    D = reservaciones(cliente= use.user,
                      cantidad_personas= request.POST.get("cantidad",""),
                      dia =request.POST.get("fecha",""),
                      restaurantes=rest.nombre)
    D.save()
    confirmadas = reservaciones.objects.filter(cantidad_personas=D.cantidad_personas)
    return render(request,'sistemareservas/hora_reserva.html',
                              {'Confirmadas':confirmadas,'usuario':use,'D':D})

def dia_reserva(request,user,pk):
    ahora = datetime.datetime.now()
    Y=ahora.year
    m=ahora.month
    d=ahora.day
    if(d<10):
        if(m<10):
            minimo="0%d-0%d-%d"%(Y,m,d)
        else:
            minimo="0%d-%d-%d"%(Y,m,d)
    else:
        if(m<10):
            minimo="%d-0%d-%d"%(Y,m,d)
        else:
            minimo="%d-%d-%d"%(Y,m,d)
    if d>28:
        Md=28
    else:
        Md=d
    if d==12:
        Mm=1
        My=Y+1
    else:
        Mm=m+1
        My=Y
    if(d<10):
        if(m<10):
            Maximo="0%d-0%d-%d"%(My,Mm,Md)
        else:
            Maximo="0%d-%d-%d"%(My,Mm,Md)
    else:
        if(m<10):
            Maximo="%d-0%d-%d"%(My,Mm,Md)
        else:
            Maximo="%d-%d-%d"%(My,Mm,Md)
    use = usuario.objects.get(user=user)
    r=Restaurantes.objects.get(pk=pk)
    return render(request,'sistemareservas/dia_reserva.html',
                  {'rest':r, 'usuario':use,'fecmin':minimo,'fecmax':Maximo})

def final(request,ident,pk):
    r=usuario.objects.get(pk=pk)
    reserva=reservaciones.objects.get(pk=ident)
    D=request.POST.get("hora","")
    reserva.hora=D
    reserva.save()
    return render(request,'sistemareservas/final.html',{'D':D, 'rest':r})
    
