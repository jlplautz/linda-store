from django.shortcuts import render

from lindaStore.carrinho.carrinho import Carrinho

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    carrinho = Carrinho(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in carrinho:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
                # Limpar o carrinho
                carrinho.clear()
                # iniciar tarefa assíncrona
                order_created.delay(order.id)

                return render(
                    request,
                    'orders/order/created.html',
                    {'order': order},
                )
    else:
        form = OrderCreateForm()
    return render(
        request,
        'orders/order/create.html',
        {'carinho': carrinho, 'form': form},
    )
