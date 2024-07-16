from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Pessoa

def index(request):

    pessoa = Pessoa.objects.filter(show=True)

    context = {
        'pessoa' : pessoa,
    }
    if request.method == 'GET':
        return render(request, 'index.html', context)

    return render(request, 'index.html', context)

def cadastrar(request):

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')

    if request.method == 'POST':
        Pessoa.objects.create(nome=nome, sobrenome=sobrenome)
        return redirect(reverse('app:index'))


def editar_pessoa(request, id):


    pessoa = get_object_or_404(Pessoa, id=id)
    
    context = {
        'pessoa' : pessoa,
    }
    if request.method == 'GET':
        return render(request, 'edit.html', context)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        pessoa=Pessoa(id=id, nome=nome, sobrenome=sobrenome)
        pessoa.save()
        
        return redirect(reverse('app:index'))

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()

    return redirect(reverse('app:index'))
