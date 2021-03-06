from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from src.item.models import Item
from src.order.models import Order


class ItemInline(GenericTabularInline):
    model = Item
    fields = ("product", "quantity", "product_price", "total_price")
    readonly_fields = ("product", "quantity", "product_price", "total_price")
    exclude = ('content_type', 'object_id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline
    ]
