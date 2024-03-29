"""
URL configuration for lindaStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from lindaStore.settings import base, local

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'carrinho/', include('lindaStore.carrinho.urls', namespace='carrinho')
    ),
    path('orders/', include('lindaStore.orders.urls', namespace='orders')),
    path('payment/', include('lindaStore.payment.urls', namespace='payment')),
    path('', include('lindaStore.shop.urls', namespace='shop')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if local.DEBUG:
    urlpatterns += static(
        base.MEDIA_URL,
        document_root=base.MEDIA_ROOT,
    )
