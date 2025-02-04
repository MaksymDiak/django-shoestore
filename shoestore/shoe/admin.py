from django.contrib import admin
from .models import Shoe, ShoeSize


class ShoeSizeInline(admin.TabularInline):
    model = ShoeSize
    extra = 1


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ["name", "brand", "price"]
    search_fields = ["name", "brand__name"]
    inlines = [ShoeSizeInline]


@admin.register(ShoeSize)
class ShoeSizeAdmin(admin.ModelAdmin):
    list_display = ["shoe", "size", "stock"]
    search_fields = ["shoe__name"]
