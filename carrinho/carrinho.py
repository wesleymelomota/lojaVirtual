from decimal import Decimal
import decimal
from core.models import Produto
from django.conf import settings

class Carrinho:

    def __init__(self, request):
        self.__sessao = request.session
        carrinho = self.__sessao.get(settings.ID_CARRINHO)
        if not carrinho:
            carrinho = self.__sessao[settings.ID_CARRINHO] = {}
        self.__carrinho = carrinho

    def adicionar(self, produto, quantidade=0, atualizar_quantidade=False):
        id_produto = str(produto.id)
        if id_produto not in self.__carrinho:
            self.__carrinho[id_produto] = {
                'quantidade': 0,
                'preco': str(produto.preco),
            }
        if atualizar_quantidade:
            self.__carrinho[id_produto]['quantidade'] = quantidade
        else:
            self.__carrinho[id_produto]['quantidade'] += quantidade
        self.__salvar()

    def __salvar(self):
        self.__sessao[settings.ID_CARRINHO] = self.__carrinho
        self.__sessao.modified = True

    def remover(self, produto):
        id_produto = str(produto.id)
        if id_produto in self.__carrinho:
            del self.__carrinho[id_produto]
            self.__salvar()

    def __iter__(self):
        ids_produto = self.__carrinho.keys()
        produtos = Produto.objects.filter(id__in=ids_produto)
        carrinho = self.__carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto']=produto
            for  item in carrinho.values():
                item['preco']=Decimal(item['preco'])
                item['subtotal']=Decimal(item['preco']) * Decimal(item['quantidade'])
                yield item
        
    def __len__(self):
        resultado = 0
        for item in self.__carrinho.values():
            resultado += item['quantidade']
        return resultado

    def limpar_carrinho(self):
        self.__sessao.flush()
        
        self.__sessao.modified = True
        

    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.__carrinho.values():
            subtotal = Decimal(item['quantidade']) * Decimal(item['preco'])
            resultado += subtotal
        return resultado

