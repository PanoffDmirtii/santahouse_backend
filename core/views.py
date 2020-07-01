from rest_framework.viewsets import ModelViewSet

from core.models import Product
from core.serializer import ProductSerializer


class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
