from django.conf.urls import url

from . import views

app_name = 'reservas'

urlpatterns = [
    url(r'^restaurantes/(?P<user>[-\w]+)/$', views.index, name='restaurantes'),
    url(r'^sistema/(?P<user>[-\w]+)/(?P<pk>[0-9]+)/$', views.principal, name='sistema'),
    url(r'^(?P<pk>[0-9]+)/informacion/$', views.info_restaurante, name='informacion'),
    url(r'^mis_reservas/$', views.mis_reservas, name='mis_reservas'),
    url(r'^hora_reserva/(?P<user>[-\w]+)/(?P<pk>[0-9]+)/$', views.hora_reserva, name='hora_reserva'),
    url(r'^dia_reserva/(?P<user>[-\w]+)/(?P<pk>[0-9]+)/$', views.dia_reserva, name='dia_reserva'),
    url(r'^final/(?P<ident>[0-9]+)/(?P<pk>[0-9]+)/$', views.final, name='final'),
    
]
