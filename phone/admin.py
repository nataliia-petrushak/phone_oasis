from django.contrib import admin
from .models import Phone, Image


admin.site.register(Image)


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
