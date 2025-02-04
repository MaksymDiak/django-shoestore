from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_items",
        "status",
        "created_at",
        "delivery_address",
    )
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "delivery_address")
    inlines = [OrderItemInline]
    ordering = ("-created_at",)
    list_editable = ("status",)

    def get_items(self, obj):
        return ", ".join(
            [f"{item.shoe.name} ({item.quantity})" for item in obj.order_items.all()]
        )

    get_items.short_description = "Items"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "shoe", "quantity")
