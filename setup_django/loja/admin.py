from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Exibe colunas específicas na listagem do Admin
    list_display = ('nome', 'preco', 'criado_em')
    
    # Adiciona uma barra de pesquisa pelo nome do produto
    search_fields = ('nome',)
    
    # Adiciona filtros laterais
    list_filter = ('criado_em',)

# Se você criou o modelo Estoque seguindo a minha sugestão anterior, 
# descomente as linhas abaixo:
# from .models import Estoque
# @admin.register(Estoque)
# class EstoqueAdmin(admin.ModelAdmin):
#     list_display = ('produto', 'quantidade')
