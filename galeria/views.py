from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Usando Dicionario de dados

# def index(request):
#     dados = {
#         1: {"nome":"Nebulosa de Carina", "legenda" : "webbtelescope.org / NASA / James Webb"},
#         2: {"nome":"Galáxia NGC 1079", "legenda" : "nasa.org / NASA / Hubble"},
#     }
    
#     return render(request, 'galeria/index.html', { "cards" : dados })

# Buscando dados do banco de dados
def index(request):
    #  Filtrando apenas as fotografias publicadas
    # Adicionando um '-' na frente do campo, troca a ordem
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    # fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', { "cards" : fotografias })

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia })

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    # Se existir o filtro, usa os dados do filtro
    if "filtro_buscar" in request.GET:
        nome_a_buscar = request.GET['filtro_buscar']
        if nome_a_buscar:
            # usando icontains e semelhante ao comando SQL 'ILIKE'
            # @see: https://docs.djangoproject.com/en/4.1/ref/models/querysets/
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards": fotografias})