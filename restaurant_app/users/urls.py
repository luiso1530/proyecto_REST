from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'login/$',views.login,name= 'login'),
    url(r'ingresar/$',views.ingresar,name= 'ingresar'),
    url(r'registrar/$',views.registrar,name= 'registrar'),
    url(r'newU/$',views.newU,name= 'newU'),
    ]
