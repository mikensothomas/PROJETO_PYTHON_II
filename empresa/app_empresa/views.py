from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.funcionarios = request.POST.get('funcionarios')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)
