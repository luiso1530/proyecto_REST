from django.conf.urls import url

from . import views

app_name = 'reservas'

urlpatterns = [
    url(r'^restaurantes/$', views.index, name='restaurantes'),
    url(r'^(?P<pk>[0-9]+)/sistema/$', views.principal, name='sistema'),
    url(r'^(?P<pk>[0-9]+)/informacion/$', views.info_restaurante, name='informacion'),
    url(r'^mis_reservas/$', views.mis_reservas, name='mis_reservas'),
    url(r'^hora_reserva/$', views.hora_reserva, name='hora_reserva'),
    url(r'^dia_reserva/$', views.dia_reserva, name='dia_reserva'),
    
]