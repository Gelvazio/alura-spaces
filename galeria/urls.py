from django.urls import path
from galeria.views import index, imagem, buscar, buscarcategoria, fotododia, curtidas, maisvistas, surpreendame, novasfotos, login, efetualogin

urlpatterns = [
    path('home', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('buscarcategoria', buscarcategoria, name='buscarcategoria'),
    path('fotododia', fotododia, name='fotododia'),
    path('curtidas/<int:foto_id>', curtidas, name='curtidas'),
    path('maisvistas', maisvistas, name='maisvistas'),
    path('surpreendame', surpreendame, name='surpreendame'),
    path('novasfotos', novasfotos, name='novasfotos'),
    # rotas de login
    path('', login, name='login'),
    path('efetualogin', efetualogin, name='efetualogin'),
]