from rest_framework.serializers import ModelSerializer

from core.models import Product, PopularProduct, Stock


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class PopularProductSerializer(ModelSerializer):

    class Meta:
        model = PopularProduct
        fields = '__all__'


class StockSerializer(ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'
