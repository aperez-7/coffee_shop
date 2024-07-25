from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class MyOrderViewTest(TestCase):
    def test_no_logged_user_should_redirect(self):
        url = reverse("my-order")
        response = self.client.get(url)
        # este assert funciona porque es una redirección; si no hubiese ninguna
        # redirección, el atributo no existiría.
        self.assertEqual(response.url, "/users/login/?next=/orders/my-order")
        self.assertEqual(response.status_code, 302)  # <- por redirección

    def test_logged_user_should_not_redirect(self):
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)

        url = reverse("my-order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
