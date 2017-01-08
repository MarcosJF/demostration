# app/urls.py

from django.conf.urls import url, include

from app import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^insertar_restaurante/$', views.insertar_restaurante, name='insertar_restaurante'),
  url(r'^buscar_restaurante/modificar_restaurante/$', views.modificar_restaurante, name='modificar_restaurante'),
  url(r'^buscar_restaurante/$', views.buscar_restaurante, name='buscar_restaurante'),
]
