from rest_framework_nested import routers

from django.urls import re_path, include

from .views import OrderViewSet

router = routers.SimpleRouter()

router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
     re_path(r'^', include(router.urls)),
]
