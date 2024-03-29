from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from lindaStore.shop.models import Product

from .carrinho import Carrinho
from .forms import CarrinhoAddProductForm


@require_POST
def carrinho_add(request, product_id):
    carrinho = Carrinho(request)
    product = get_object_or_404(Product, id=product_id)
    form = CarrinhoAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        carrinho.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update'],
        )

    return redirect('carrinho:carrinho_detail')


def carrinho_remove(request, product_id):
    carrinho = Carrinho(request)
    product = get_object_or_404(Product, id=product_id)
    carrinho.remove(product)
    return redirect('carrinho:carrinho_detail')


def carrinho_detail(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['update_quantity_form'] = CarrinhoAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True,
            }
        )
    return render(request, 'carrinho/detail.html', {'carrinho': carrinho})
