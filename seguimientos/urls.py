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
    #path('usuarios/registro', views.registro, name='registro'),
    path('administrador', views.administador, name='administrador'),
    path('agente', views.agente, name='agente'),
    path('nuevatarea',views.nuevatarea, name='nuevatarea'),
    path('areaGestion',views.areaGestion,name='areaGestion'),
    path('nuevaAreaGstion',views.nuevaAreaGestion,name='nuevaAreaGestion'),
    path('cliente',views.cliente,name='cliente'),
    path('nuevoCliente',views.nuevoCliente,name='nuevoCliente'),
    path('ciudad',views.ciudad,name='ciudad'),
    path('nuevaCiudad',views.nuevaCiudad,name='nuevaCiudad'),
    path('estado',views.estado,name='estado'),
    path('nuevoEstado',views.nuevoEstado,name='nuevoEstado'),
    path('ingeniero',views.ingeniero,name='ingeniero'),
    path('nuevoIngeniero',views.nuevoIngeniero,name='nuevoIngeniero'),
    path('rol',views.rol,name='rol'),
    path('nuevoRol',views.nuevoRol,name='nuevoRol'),
    path('tecnico',views.tecnico,name='tecnico'),
    path('nuevoTecnico',views.nuevoTecnico,name='nuevoTecnico'),
    path('tipoTarea',views.tipoTarea,name='tipoTarea'),
    path('nuevoTipoTarea',views.nuevoTipoTarea,name='nuevoTipoTarea'),
    path('tipoUsuario',views.tipoUsuario,name='tipoUsuario'),
    path('nuevoTipoUsuario',views.nuevoTipoUsuario,name='nuevoTipoUsuario'),
    path('tipoEstado',views.tipoEstado,name='tipoEstado'),
    path('nuevoTipoEstado',views.nuevoTipoEstado,name='nuevoTipoEstado'),
    path('usuario',views.usuario,name='usuario'),
    path('nuevoUsuario',views.nuevoUsuario,name='nuevoUsuario'),
    path('zonaUsuario',views.zonaUsuario,name='zonaUsuario'),
    path('nuevaZonaUsuario',views.nuevaZonaUsuario,name='nuevaZonaUsuario'),
    path('zona',views.zona,name='zona'),
    path('nuevaZona',views.nuevaZona,name='nuevaZona')

]
