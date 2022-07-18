from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.
def home(request):
    listaUsuarios = Usuario.objects.all()
    messages.success(request, 'Cursos listados')
    return render(request, "gestionUsuarios.html", {"usuarios": listaUsuarios})

def registrarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']

    usuario=Usuario.objects.create(codigo=codigo, nombre=nombre, apellido=apellido)
    messages.success(request, 'Curso registrado')
    return redirect('/')

def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    usuario.delete()
    messages.success(request, 'Curso eliminado')

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
    messages.success(request, 'Curso modificado')

    return redirect('/')