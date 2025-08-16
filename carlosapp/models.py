from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    preco = models.DecimalField("Preço atual", max_digits=10, decimal_places=2)
    subi_preco = models.DecimalField("Preço anterior", max_digits=10, decimal_places=2, null=True, blank=True)
    estoque = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='imagens')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"   