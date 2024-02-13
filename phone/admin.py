from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "screen",
        "resolution",
        "processor",
        "camera",
        "zoom",
        "cell",
        "about",
    )
