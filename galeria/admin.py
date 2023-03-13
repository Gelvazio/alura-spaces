from django.contrib import admin

from galeria.models import Fotografia

# Personalizando a visualização
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    # Adicionando campos que serão links
    list_display_links = ("id","nome")
    # Adicionando campo de busca
    search_fields = ("nome",)
    # Adicionando novo filtro 'categoria'
    list_filter = ("categoria",)
    # Adicionando paginação
    list_per_page = 3
    # Alterando coluna na consulta
    list_editable = ("publicada",)
    

admin.site.register(Fotografia, ListandoFotografias)