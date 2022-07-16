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