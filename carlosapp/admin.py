from django.contrib import admin
from .models import Categoria, Produto, Pedido, ItemPedido

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Categoria, CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'preco','subi_preco', 'estoque', 'categoria')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome', 'descricao')
    list_filter = ('categoria',)

admin.site.register(Produto, ProdutoAdmin)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

admin.site.register(ItemPedido)   

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'finalizado')
    list_filter = ('finalizado', 'data')
    inlines = [ItemPedidoInline]

admin.site.register(Pedido, PedidoAdmin)