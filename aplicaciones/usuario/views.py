from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    listaUsuarios = Usuario.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": listaUsuarios})