from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Produto
from .carrinho import Carrinho
from .forms import FormAdicionarProdutoCarrinho 

# Create your views here.
@require_POST
def adicionar_ao_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    form = FormAdicionarProdutoCarrinho(request.POST)

    if form.is_valid():
        dados = form.cleaned_data
        carrinho.adicionar(produto=produto,
        quantidade=dados['quantidade'],
        atualizar_quantidade=dados['atualizar'])
    
    return redirect('carrinho:detalhes_carrinho')

def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('carrinho:detalhes_carrinho')

def detalhes_carrinho(request):
    carrinho = Carrinho(request)
    list_produtos = []
    lista_produtos_filtrados = []
    for item in carrinho:
        item['formulario_adicionar_produto_ao_carrinho'] = FormAdicionarProdutoCarrinho(
            initial={'quantidade': item['quantidade'],
            'atualizar': True}
        )
        list_produtos.append(item)
    for item in list_produtos:
        if item not in lista_produtos_filtrados:
            lista_produtos_filtrados.append(item)
        
    return render(request, 'carrinho/detalhes.html', {'carrinho': lista_produtos_filtrados, 'valorTotal': carrinho})