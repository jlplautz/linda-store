from django.urls import path

from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho_detail, name='carrinho_detail'),
    path('add/<int:product_id>', views.carrinho_add, name='carrinho_add'),
    path(
        'remove/<int:product_id>',
        views.carrinho_remove,
        name='carrinho_remove',
    ),
]
