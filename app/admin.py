# Register your models here.
# app/admin.py

from django.contrib import admin
from .models import Estado, Cidade, Endereco, Categoria, Evento, Cliente, Telefone, Produto, Pedido, ItemPedido, Pagamento, PagamentoBoleto, PagamentoCartao

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id_estado', 'nome_estado']
    search_fields = ['nome_estado']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['id_cidade', 'nome_cidade', 'estado']
    search_fields = ['nome_cidade', 'estado__nome_estado']
    list_filter = ['estado']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['id_endereco', 'local', 'cidade']
    search_fields = ['cidade__nome_cidade']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria', 'nome_categoria']
    search_fields = ['nome_categoria']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id_evento', 'nome_evento', 'descricao', 'endereco', 'categoria']
    search_fields = ['nome_evento', 'descricao', 'endereco__cidade__nome_cidade', 'categoria__nome_categoria']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'nome', 'cpf_cnpj', 'email', 'tipo_cliente']
    search_fields = ['nome', 'cpf_cnpj', 'email']
    list_filter = ['tipo_cliente']

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['id_telefone', 'numero', 'cliente']
    search_fields = ['numero', 'cliente__nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id_produto', 'nome', 'preco']
    search_fields = ['nome']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id_pedido', 'data_pedido', 'cliente']
    list_filter = ['data_pedido']

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['id_item_pedido', 'pedido', 'produto', 'preco', 'desconto', 'quantidade']
    search_fields = ['pedido__id_pedido', 'produto__nome']

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['id_pagamento', 'estado', 'pedido']
    list_filter = ['estado']

@admin.register(PagamentoBoleto)
class PagamentoBoletoAdmin(admin.ModelAdmin):
    list_display = ['pagamento', 'data_vencimento', 'data_pagamento']

@admin.register(PagamentoCartao)
class PagamentoCartaoAdmin(admin.ModelAdmin):
    list_display = ['pagamento', 'num_parcelas']
