"""proyecto_restaurantes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from sistemareservas import views
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurantes/$', views.index, name='restaurantes'),
    url(r'^(?P<pk>[0-9]+)/sistema/$', views.principal, name='sistema'),
    url(r'^(?P<pk>[0-9]+)/informacion/$', views.info_restaurante, name='informacion'),
    url(r'^mis_reservas/$', views.mis_reservas, name='mis_reservas'),
    url(r'^(?P<pk>[0-9]+)/hora_reserva/$', views.hora_reserva, name='hora_reserva'),
    url(r'^(?P<pk>[0-9]+)/dia_reserva/$', views.dia_reserva, name='dia_reserva'),
    url(r'^(?P<pk>[0-9]+)/final/$', views.final, name='final'),
    
]
