from django.contrib import admin

from .models import Order, OrderHasProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderHasProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
