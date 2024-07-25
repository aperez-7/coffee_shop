from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductListViewTest(TestCase):
    def test_should_return_200(self):
        """Prueba del código de regreso de la vista de listado de productos."""
        url = reverse("list_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object_list"].count(), 0)

    def test_should_return_200_with_products(self):
        """Prueba del código de regreso de la vista de listado de productos."""
        Product.objects.create(
            name="Chocomilk", description="Muy rico uwuwu", price=25.0, available=True
        )

        url = reverse("list_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object_list"].count(), 1)
