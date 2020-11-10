from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from products.api.v1.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product


class CategoryResource(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = []
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'related_category',
    ]
    search_fields = [
        'name',
    ]
    ordering_fields = [
        'id',
        'created_at',
        'related_category',
    ]


class ProductResource(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = []
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'code',
        'name',
    ]
    ordering_fields = [
        'id',
        'price',
        'quantity',
        'created_at',
    ]
