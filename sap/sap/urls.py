"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from clientes.views import agregar, modificar, ver, eliminar, generar_reporte, ClienteViewSet, PedidoViewSet, ProductoViewSet
from rest_framework import routers
from webapp.views import bienvenida, despedida, bienvenida2

router = routers.DefaultRouter()
router.register(r'api_cliente', ClienteViewSet)
router.register(r'api_pedido', PedidoViewSet)
router.register(r'api_producto', ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('bienvenido/',bienvenida),
    # path('despedida/',despedida),
    path('', bienvenida2, name='inicio'),
    path('agregar/', agregar, name='agregar'),
    path('modificar/<int:id>/', modificar, name='modificar'),
    path('ver/<int:id>/', ver, name='ver'),
    path('eliminar/<int:id>', eliminar),
    path('generar_reporte/', generar_reporte),
]

urlpatterns += router.urls
