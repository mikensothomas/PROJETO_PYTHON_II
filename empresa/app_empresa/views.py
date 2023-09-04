from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.funcionarios = request.POST.get('funcionarios')
    novo_usuario.clientes = request.POST.get('clientes')
    novo_usuario.fornecedores = request.POST.get('fornecedores')
    novo_usuario.produtos = request.POST.get('produtos')
    novo_usuario.empresas_terceiras = request.POST.get('empresas_terceiras')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)
