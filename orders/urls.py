from django.urls import path

from .views import *


urlpatterns = [
    path("my-order", MyOrderView.as_view(), name="my-order"),
    path("add-product", AddOrderProductView.as_view(), name="add-product"),
    ##### VISTAS DE API #####
    path("api/v1/create_order", CreateOrderAPI.as_view(), name="create-order"),
]
