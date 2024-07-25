from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics as drf_generic
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductFormView(generic.FormView):
    """Vista para el formulario que agrega un producto a BD."""

    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_products")

    def form_valid(self, form: ProductForm):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/list_products.html"
    model = Product


class ProductListAPI(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CreateProductAPI(drf_generic.CreateAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return Response(status=200)
