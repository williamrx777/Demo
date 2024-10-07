from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.messages import constants
def index(request):
    if request.method == "GET":
        filmes = Filme.objects.all()
        return render(request, 'index.html', {'filmes': filmes})

    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        lancamento = request.POST.get('lancamento')
        link = request.POST.get('link')

        filme = Filme(nome=nome, descricao=descricao, lancamento=lancamento, link=link)
        filme.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect('index')

def delete_filme(request, codigo):
    filme = get_object_or_404(Filme, codigo=codigo)
    filme.delete()
    messages.add_message(request, constants.SUCCESS, 'Filme deletado com sucesso')
    return redirect('index')

def update_filme(request, codigo):
    filme = get_object_or_404(Filme, codigo=codigo)
    if request.method == "POST":
        filme.nome = request.POST.get('nome')
        filme.descricao = request.POST.get('descricao')
        filme.lancamento = request.POST.get('lancamento')
        filme.link = request.POST.get('link')
        filme.save()
        messages.add_message(request, constants.SUCCESS, 'Filme atualizado com sucesso')
        return redirect('index')
    return render(request, 'update.html', {'filme': filme})