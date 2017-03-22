
from django.conf.urls import url
from django.contrib import admin

from .views import ProductDetail, ProductList, VariationList

urlpatterns = [
    url(r'^$', ProductList.as_view(), name="products"),
    url(r'^(?P<pk>\d+)$', ProductDetail.as_view(), name="product_detail"),
    url(r'^(?P<pk>\d+)/inventory/$', VariationList.as_view(), name="product_inventory"),
]
