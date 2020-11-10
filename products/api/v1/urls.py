from rest_framework.routers import DefaultRouter
from products.api.v1.views import (
    CategoryResource,
    ProductResource,
)

router = DefaultRouter()
router.register(r'categories', CategoryResource, basename='categories')
router.register(r'products', ProductResource, basename='products')

urlpatterns = []

urlpatterns += router.urls
