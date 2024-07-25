from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics as drf_generics
from rest_framework.response import Response

from .forms import OrderHasProductForm
from .models import Order
from .serializers import OrderSerializer


class MyOrderView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset: QuerySet = None):
        """Sobreescribimos este método para mostrar orden."""
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class AddOrderProductView(LoginRequiredMixin, generic.CreateView):
    template_name = "orders/add_order_product.html"
    form_class = OrderHasProductForm
    success_url = reverse_lazy("my-order")

    def form_valid(self, form: OrderHasProductForm):
        order, created = Order.objects.get_or_create(
            is_active=True, user=self.request.user
        )
        form.instance.order = order
        form.instance.quantity = 1
        # form.instance.product se inyecta desde la template
        form.save()

        return super().form_valid(form)


class CreateOrderAPI(drf_generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(
        self,
        request,
    ):
        return Response(status=200)
