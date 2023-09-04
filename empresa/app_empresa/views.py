from django.shortcuts import render

def home(request):
    return render(request,'dados/home.html')

def funcionarios(request):
    novo_funcionario = funcionarios()
    novo_funcionario.funcionarios = request.POST.get('Funcionarios')
    novo_funcionario.save()

    funcionarios = {
        'funcionarios': funcionarios.objects.all()
    }

    return render(request,'dados/usuarios.html',funcionarios)
