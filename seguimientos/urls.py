"""seguimientos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/login',views.login,name='login'),
    path('',views.index, name='index'),
    path("admin/", admin.site.urls),
    path('usuarios/salir',views.salir, name='salir'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/administrador', views.administador, name='administrador'),
    path('usuarios/agente', views.agente, name='agente'),
    path('usuarios/nuevatarea',views.nuevatarea, name='nuevatarea'),
    path('usuarios/areaGestion',views.areaGestion,name='areaGestion'),
    path('usuarios/nuevaAreaGstion',views.nuevaAreaGestion,name='nuevaAreaGestion'),
    path('usuarios/cliente',views.cliente,name='cliente'),
    path('usuario/nuevoCliente',views.nuevoCliente,name='nuevoCliente'),
    path('usuarios/ciudad',views.ciudad,name='ciudad'),
    path('usuarios/nuevaCiudad',views.nuevaCiudad,name='nuevaCiudad'),
    path('usuario/estado',views.estado,name='estado'),
    path('usuario/nuevoEstado',views.nuevoEstado,name='nuevoEstado'),
    path('usuario/ingeniero',views.ingeniero,name='ingeniero'),
    path('usuario/nuevoIngeniero',views.nuevoIngeniero,name='nuevoIngeniero'),
    path('usuario/rol',views.rol,name='rol'),
    path('usuario/nuevoRol',views.nuevoRol,name='nuevoRol'),
    path('usuario/tecnico',views.tecnico,name='tecnico'),
    path('usuario/nuevoTecnico',views.nuevoTecnico,name='nuevoTecnico'),
    path('usuario/tipoTarea',views.tipoTarea,name='tipoTarea'),
    path('usuario/nuevoTipoTarea',views.nuevoTipoTarea,name='nuevoTipoTarea'),
    path('usuario/tipoUsuario',views.tipoUsuario,name='tipoUsuario'),
    path('usuario/nuevoTipoUsuario',views.nuevoTipoUsuario,name='nuevoTipoUsuario'),
    path('usuario/tipoEstado',views.tipoEstado,name='tipoEstado'),
    path('usuario/nuevoTipoEstado',views.nuevoTipoEstado,name='nuevoTipoEstado'),
    path('usuario/usuario',views.usuario,name='usuario'),
    path('usuario/nuevoUsuario',views.nuevoUsuario,name='nuevoUsuario'),
    path('usuario/zonaUsuario',views.zonaUsuario,name='zonaUsuario'),
    path('usuario/nuevaZonaUsuario',views.nuevaZonaUsuario,name='nuevaZonaUsuario'),
    path('usuario/zona',views.zona,name='zona'),
    path('usuario/nuevaZona',views.nuevaZona,name='nuevaZona')

]
