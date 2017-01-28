from django.conf.urls import url

from . import views

app_name = 'owner'

urlpatterns = [
	url(r'^(?P<own>[-\w]+)/$',views.principal,name = 'principal'),
        url(r'^(?P<own>[-\w]+)/peticiones/$',views.peticiones,name = 'peticiones'),
]
