from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout  
from .forms import NuevoUsuario
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html',{
        'mensaje': 'Ingreso de Personas',
        'titulo': 'Personas',
        'personas': [
            {'titulo':'Maria','Edad':15, 'adulto':False},
            {'titulo':'Matias','Edad':24, 'adulto':True},
            {'titulo':'Jorge','Edad':11, 'adulto':False},
            {'titulo':'Marta','Edad':44, 'adulto':True}
        ]
    })

def login(request):
    if request.user.is_authenticated:
        return redirect('administrador')
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        password = request.POST.get('password')

        usuarios = authenticate(nombreUsuario=nombreUsuario, password=password)
        if usuarios:
            lg(request,usuarios)
            messages.success(request, f'Bienvenido {usuarios.username}')
            return redirect('administrador')
        else:
            messages.error(request, 'Datos Incorrectos')

    return render(request,'users/login.html',{})


def salir(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect(login)

# def registro(request):
#     form = Registro(request.POST or None)
#     if request.method=='POST' and form.is_valid():
        

#         usuario = form.save()
#         if usuario:
#             lg(request, usuario)
#             messages.success(request, 'Bienvenido')
#             return redirect('administrador')

#    return render(request, 'users/registro.html')
# {
#         'form':form

#         })

def administador(request):
    return render(request,'administrador.html')

def agente(request):
    return render(request, 'agente.html')

def nuevatarea(request):
    return render(request,'nuevatarea.html')

def areaGestion(request):
    return render(request,'areaGestion.html')    

def nuevaAreaGestion(request):
    return render(request,'nuevaAreaGestion.html')        

def cliente(request):
    return render(request,'cliente.html')   

def nuevoCliente(request):
    return render(request,'nuevoCliente.html')  

def ciudad(request):
    return render(request,'ciudad.html')    

def nuevaCiudad(request):
    return render(request,'nuevaCiudad.html')

def estado(request):
    return render(request,'estado.html')

def nuevoEstado(request):
    return render(request,'nuevoEstado.html')

def ingeniero(request):
    return render(request,'ingeniero.html')

def nuevoIngeniero(request):
    return render(request,'nuevoIngeniero.html')

def rol(request):
    return render(request,'rol.html')

def nuevoRol(request):
    return render(request,'nuevoRol.html')

def tecnico(request):
    return render(request,'tecnico.html')

def nuevoTecnico(request):
    return render(request,'nuevoTecnico.html')

def tipoTarea(request):
    return render(request,'tipoTarea.html')

def nuevoTipoTarea(request):
    return render(request,'nuevoTipoTarea.html')

def tipoUsuario(request):
    return render(request,'tipoUsuario.html')

def nuevoTipoUsuario(request):
    return render(request,'nuevoTipoUsuario.html')        

def tipoEstado(request):
    return render(request,'tipoEstado.html')

def nuevoTipoEstado(request):
    return render(request,'nuevoTipoEstado.html')

def usuario(request):
    return render(request,'usuario.html')

def nuevoUsuario(request):
    form = NuevoUsuario(request.POST or None)
    if request.method=='POST' and form.is_valid():
   
        
        usuario = form.save()                       
        if usuario:
            lg(request,usuario)
            messages.success(request,'Bienvenido')
            return redirect('usuario.html')
        
    return render(request,'nuevoUsuario.html',{
        'form':form
    })
    
    

def zonaUsuario(request):
    return render(request,'zonaUsuario.html')

def nuevaZonaUsuario(request):
    return render(request,'nuevaZonaUsuario.html')    

def zona(request):
    return render(request,'zona.html')

def nuevaZona(request):
    return render(request,'nuevaZona.html')



