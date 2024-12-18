from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def meus_materiais(request):
    return render(request, "meus_materiais.html")

def area_usuario(request):
    return render(request, "area_usuario.html")

def sobre_nos(request):
    return render(request, "sobre_nos.html")

def configuracoes(request):
    return render(request, "configuracoes.html")

def conteudos(request):
    return render(request, "conteudos.html")