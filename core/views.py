from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from core import forms
from core.models import Produto, Categoria
from carrinho.forms import FormAdicionarProdutoCarrinho

# Create your views here.
class ViewFaleConosco(FormView):
    template_name = "faleConosco.html"
    form_class = forms.FaleConoscoForm
    success_url = "/"

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)

def index(request):
    produtos = Produto.objects.filter(promocao=True)
    return render(request, 'index.html', {'produtos': produtos})

def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categoria = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)
    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categoria,
        'lista_produtos': lista_produtos
    }
    return render(request, 'produto/listar.html', contexto)
#acrescentar o id
def detalhes_produtos(request, slug_produto, id):
    produto = get_object_or_404(Produto, id=id, slug=slug_produto, disponivel=True)
    form_adicionar_produto_ao_carrinho = FormAdicionarProdutoCarrinho()
    contexto = {
        'produto': produto,
        'form_produto_carrinho': form_adicionar_produto_ao_carrinho
    }
    return render(request, 'produto/detalhes.html', contexto)
