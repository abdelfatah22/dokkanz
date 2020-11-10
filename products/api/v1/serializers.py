from rest_framework import serializers

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'related_count',
        ]


class CategoryDetailsSerializer(CategorySerializer):

    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name,
            'related_count': value.related_count(),
        }


class ProductSerializer(serializers.ModelSerializer):
    categories = CategoryDetailsSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'code',
            'name',
            'price',
            'quantity',
            'categories',
        ]
