from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def home(request):
    listaUsuarios = Usuario.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": listaUsuarios})

def registrarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']

    usuario=Usuario.objects.create(codigo=codigo, nombre=nombre, apellido=apellido)
    return redirect('/')

def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    usuario.delete()

    return redirect('/')

def edicionUsuario(request,codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    return render(request, "edicionUsuarios.html", {"usuario":usuario})

def editarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']

    usuario = Usuario.objects.get(codigo=codigo)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.save()

    return redirect('/')