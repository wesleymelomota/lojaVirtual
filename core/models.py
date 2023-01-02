from django.db import models
from django.urls import reverse
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataUltimaAtualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("core:listar_produtos_por_categoria", args=[self.slug])
    

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    promocao = models.BooleanField(default=False)
    estoque = models.PositiveIntegerField()
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataUltimaAtualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True)

    class Meta:
        ordering = ('nome', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('core:detalhes_produto', args=[self.slug, self.id])
