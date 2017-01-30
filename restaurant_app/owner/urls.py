from django.conf.urls import url

from . import views

app_name = 'owner'

urlpatterns = [
	url(r'^(?P<own>[-\w]+)/$',views.principal,name = 'principal'),
        url(r'^(?P<own>[-\w]+)/peticiones/$',views.peticiones,name = 'peticiones'),
        url(r'^(?P<own>[-\w]+)/solicitud/(?P<pk>[0-9]+)/$',views.solicitudes,name = 'solicitudes'),
        url(r'^(?P<own>[-\w]+)/solicitud_fecha/$',views.solicitud_fecha,name='sol_fecha'),
]
