from rest_framework import routers
from core.views import ProductList, PopularProductList, StockList

router = routers.SimpleRouter()
router.register('product', ProductList)
router.register('popular', PopularProductList)
router.register('stock', StockList)

urlpatterns = router.urls
