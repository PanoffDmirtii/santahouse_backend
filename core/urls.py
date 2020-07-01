from django.urls import path
from rest_framework import routers

from core import views
from core.views import ProductList

router = routers.SimpleRouter()
router.register('products', ProductList)

urlpatterns = router.urls


