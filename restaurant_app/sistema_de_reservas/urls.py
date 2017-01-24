from django.conf.urls import url

from . import views

app_name = 'reservas'

urlpatterns = [
    url(r'^restaurantes/$', views.index, name='restaurantes'),
    url(r'^sistema/$', views.principal, name='system'),
    url(r'^informacion/$', views.info_restaurante, name='informacion'),
    
]