from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'preco', 'estoque', 'disponivel', 'promocao', 'dataCriacao', 'dataUltimaAtualizacao']
    list_filter = ['disponivel', 'dataCriacao', 'dataUltimaAtualizacao']
    list_editable = ['preco', 'estoque', 'disponivel']
    prepopulated_fields = {'slug': ('nome',)}