from apps.orders.api.v1 import urls

from django.urls import include, re_path

urlpatterns = [
    re_path(r'^api/v1/', include('apps.orders.api.v1.urls')),
]
