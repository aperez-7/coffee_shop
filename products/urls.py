from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("add_product/", ProductFormView.as_view(), name="add_product"),
    path("list_products/", ProductListView.as_view(), name="list_products"),
    ##### RUTAS DE LA API #####
    path("api/v1/get_all", ProductListAPI.as_view(), name="list_products_api"),
    path(
        "api/v1/create_product", CreateProductAPI.as_view(), name="create_product_api"
    ),
]
