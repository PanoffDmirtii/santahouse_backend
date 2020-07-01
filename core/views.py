from rest_framework.viewsets import ModelViewSet

from core.models import Product, PopularProduct, Stock
from core.serializer import ProductSerializer, PopularProductSerializer, StockSerializer


class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PopularProductList(ModelViewSet):
    queryset = PopularProduct.objects.all()
    serializer_class = PopularProductSerializer


class StockList(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
