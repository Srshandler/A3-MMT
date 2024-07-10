from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nome_estado = models.CharField(max_length=255)


class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome_cidade = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    local = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255)


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Cliente(AbstractUser): # Recebe usuario já feito do django
    # Your custom fields for Cliente
    class TipoCliente(models.IntegerChoices):
        PESSOA_FISICA = 1, 'Pessoa Física'
        PESSOA_JURIDICA = 2, 'Pessoa Jurídica'

    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    tipo_cliente = models.IntegerField(
        choices=TipoCliente.choices,
        default=TipoCliente.PESSOA_FISICA,
    )
    username = None
    USERNAME_FIELD = 'cpf_cnpj'
    REQUIRED_FIELDS = ['nome', 'email', 'tipo_cliente']

    # Define related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(Group, related_name='clientes')
    user_permissions = models.ManyToManyField(Permission, related_name='clientes')

    def __str__(self):
        return self.cpf_cnpj  # Or any other representation you prefer


class Telefone(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    preco = models.FloatField()


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_pedido = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class ItemPedido(models.Model):
    id_item_pedido = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField()
    desconto = models.FloatField()
    quantidade = models.IntegerField()


class Pagamento(models.Model):
    class EstadoPagamento(models.IntegerChoices):
        PENDENTE = 1, 'Pendente'
        QUITADO = 2, 'Quitado'
        CANCELADO = 3, 'Cancelado'


    id_pagamento = models.AutoField(primary_key=True)
    estado = models.IntegerField(
        choices=EstadoPagamento.choices,
        default=EstadoPagamento.PENDENTE,
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


class PagamentoBoleto(models.Model):
    pagamento = models.OneToOneField(Pagamento, on_delete=models.CASCADE, primary_key=True)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()


class PagamentoCartao(models.Model):
    pagamento = models.OneToOneField(Pagamento, on_delete=models.CASCADE, primary_key=True)
    num_parcelas = models.IntegerField()