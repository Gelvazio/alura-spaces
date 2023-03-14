from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    
    fotografia.visitas = fotografia.visitas + 1
    fotografia.save()
    
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def buscarcategoria(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscarcategoria" in request.GET:
        valor_a_buscar = request.GET['buscarcategoria']
        if valor_a_buscar:
            fotografias = fotografias.filter(categoria__icontains=valor_a_buscar)

    return render(request, "galeria/buscar_por_tipo.html", {"cards": fotografias})

def fotododia(request):
    return render(request, "galeria/nasafile.html")

def curtidas(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    # Adicionando mais uma curtida na foto
    fotografia.curtidas = fotografia.curtidas + 1
    
    fotografia.save()
        
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def maisvistas(request):
    # Lista apenas os 4 primeiros registros de fotos publicadas
    fotografias = Fotografia.objects.order_by('curtidas').filter(publicada=True)[:4]

    return render(request, "galeria/buscar.html", {"cards": fotografias})

