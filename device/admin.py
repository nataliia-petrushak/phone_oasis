from django.contrib import admin
from .models import Color, Memory, Image, Category


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hex_value")


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ("id", "ram", "capacity", "price")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "device_name", "url")


admin.site.register(Category)
