from django.urls import path 
from clientes_app import views
urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente")
]
