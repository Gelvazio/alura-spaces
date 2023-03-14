from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

import random, sqlite3

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

# def admin(request):
#     fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
#     return render(request, 'galeria/index.html', {"cards": fotografias})

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

    return render(request, "galeria/buscar.html", {"cards": fotografias})

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
  
def surpreendame(request):
    lista_fotografias = Fotografia.objects.order_by('id').filter(publicada=True)
    
    # Pega o total de fotos
    total_fotografias = lista_fotografias.count()
    
    # Faz um random das fotos e retorna apenas uma foto
    foto_sorteada = random.randint(1, total_fotografias)
    
    fotografia_sorteada = None
    nome_foto_sorteada = "Tente de novo!"
    for fotografia in lista_fotografias:
        if foto_sorteada == fotografia.id:
            fotografia_sorteada = fotografia
            nome_foto_sorteada = fotografia.nome
            break
    
    if fotografia_sorteada:
        # Transforma num array
        fotografias = [fotografia_sorteada]     
    else:
        fotografias = lista_fotografias
        
    return render(request, "galeria/buscar.html", {"foto_sorteada": nome_foto_sorteada, "cards": fotografias})

def novasfotos(request):
    # Connecting to sqlite
    conn = sqlite3.connect('db.sqlite3')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Retrieving specific records using the where clause
    # Retorna apenas as fotos cadastradas na data atual 
    cursor.execute("SELECT * from galeria_fotografia WHERE data_fotografia >= current_date and publicada = 1")
    
    fotografias = cursor.fetchall()

    lista_fotografias = []
    for foto in fotografias:
        print(foto)
        foto_id = foto[0]
        fotografia = get_object_or_404(Fotografia, pk=foto_id)
        lista_fotografias.append(fotografia)

    # Closing the connection
    conn.close()
    
    return render(request, "galeria/buscar.html", {"cards": lista_fotografias})




