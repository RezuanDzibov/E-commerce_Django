from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from item.models import Item

from .models import Cart


class ItemInline(GenericTabularInline):
    model = Item
    fields = ("product", "quantity", "item_price", "total_price")
    readonly_fields = ("product", "item_price", "total_price")
    exclude = ('content_type', 'object_id',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)