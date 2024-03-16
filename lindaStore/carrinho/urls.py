from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho_detail, name='cart_detail'),
    path('add/<slug:product_slug>', views.carrinho_add, name='carrinho_add'),
    path('remove/<slug:product_slug>', views.carrinho_remove, name='carrinho_remove'),
]
