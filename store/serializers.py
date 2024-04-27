from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )

class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = (
            'id',
            'product',
            'material',
            'quantity',
            'created_at',
            'updated_at',
        )

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = (
            'id',
            'material',
            'remainder',
            'price',
            'created_at',
            'updated_at',
        )

class ProductSerializer(serializers.ModelSerializer):
    materials = ProductMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
