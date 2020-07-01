from django.contrib import admin

from core.models import Product, PopularProduct, Stock

admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(Stock)
