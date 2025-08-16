from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'carlosapp/index.html', context)

def eletronica(request,nome_categoria):

    categoria = get_object_or_404(Categoria, nome=nome_categoria)
    
    produtos = Produto.objects.filter(categoria=categoria)
   
    return render(request, 'carlosapp/eletronica.html', {
        'produtos': produtos,
        'categoria': categoria
    })

def casa(request):
    return render(request, 'carlosapp/casa.html')

def automotivo(request):
    return render(request, 'carlosapp/automotivo.html')

def ferramentas(request):
    return render(request, 'carlosapp/ferramentas.html')

def esporte_lazer(request):
    return render(request, 'carlosapp/esporte_lazer.html')

def brinquedos(request):
    return render(request, 'carlosapp/brinquedos.html')

def eletrodomesticos(request):
    return render(request, 'carlosapp/eletrodomesticos.html')

