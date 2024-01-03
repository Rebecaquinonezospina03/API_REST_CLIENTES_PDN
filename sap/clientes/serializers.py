from rest_framework import serializers

from clientes.models import Pedido, Producto, Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'fecha_pedido', 'tipo_producto', 'numero_de_pedido')


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'id','tipo_producto','descripcion','precio','existencias','fecha_creacion')


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('url', 'cliente', 'descripcion', 'estado', 'total', 'pagado', 'numero')
