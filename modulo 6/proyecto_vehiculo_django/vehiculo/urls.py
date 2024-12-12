from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.agregar, name='agregar'),
    path('vehiculo/listado/', views.listar, name='listar'),
]
