from django.contrib import admin
from .models import Tablet


@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "screen",
        "resolution",
        "processor",
        "camera",
        "about",
    )
