from django.forms import ModelForm

from .models import OrderHasProduct


class OrderHasProductForm(ModelForm):
    class Meta:
        model = OrderHasProduct
        fields = ["product"]  # este es el único dato disponible en la vista
