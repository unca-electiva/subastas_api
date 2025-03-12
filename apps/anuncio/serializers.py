from rest_framework import serializers
from .models import Anuncio, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'activa'
        ]

    def validate_nombre(self, value):
        """
        Verificar que el nombre no contegna la palabra "categoría"
        """

        if "categoria" in value.lower():
            raise serializers.ValidationError("El nombre no puede contener la palabra 'categoria'.")
        return value

    def validate(self, data):
        if 'principal' in data['nombre'].lower() and not data['activa']:
            raise serializers.ValidationError("No se puede desactivar la Categoria principal")
        return data


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            'id',
            'titulo',
            'descripcion',
            'precio_inicial',
            'imagen',
            'fecha_inicio',
            'activo',
            'categorias',
        ]
