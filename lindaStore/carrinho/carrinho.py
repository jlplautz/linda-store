from decimal import Decimal
from django.conf import settings
from lindaStore.shop.models import Product


class Carrinho(object):
    def __init__(self, request):
        """
        Initializar o carrinho.
        """
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not carrinho:
            # salvar o carrinho vazio dentro da sessão
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        
        self.carrinho = carrinho


    def add(self, product, quantity=1, update_quantity=False):
        """
        Adicionar u produto no carrinho ou fazer atualização da quantidade.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.carrinho[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.carrinho[product_id]['quantity'] = quantity
        else:
            self.carrinho[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Atualizar a sessão do carrinho.
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
        # marcar a sessão como "modificada" para ter certeza que foi salva.
        self.session.modified = True

    def remove(self, product):
        """
        Retirar um produto do carrinho.
        """
        product_id = str(product.id)
        if product_id in self.carrinho:
            del self.carrinho[product_id]
            self.save()

    def __iter__(self):
        """
        Iterar sobre os itens dentro do carrinho e obter os produtos do banco de dados.
        """
        product_ids = self.carrinho.keys()

        # Obter os produtos e adicioná-los no carrinho.
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.carrinho[str(product.id)]['product'] = product

        for item in self.carrinho.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Contar todos os itens do carrinho.
        """
        return sum(item['quantity'] for item in self.carrinho.values())

    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.carrinho.values())
    
    def clear(self):
        # remover o carrinho da sessão
        del self.session[settings.CARRINHO_SESSION_ID]
        self.session.modified = True