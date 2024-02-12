from rest_framework import serializers
from .models import Memory, Color, Phone


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ("id", "ram", "built_in", "price")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name", "hex_value")


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = (
            "id",
            "name",
            "memories",
            "colors",
            "screen",
            "resolution",
            "processor",
            "camera",
            "zoom",
            "cell",
            "about"
        )


class PhoneListSerializer(PhoneSerializer):
    memories = MemorySerializer(many=True, read_only=True)

    class Meta:
        model = Phone
        fields = ("id", "name", "screen", "memories", "in_cart", "is_favourite")


class PhoneDetailSerializer(PhoneListSerializer):
    memories = MemorySerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    images = serializers.SlugRelatedField(slug_field="url", many=True, read_only=True)

    class Meta:
        model = Phone
        fields = (
            "id",
            "name",
            "memories",
            "colors",
            "screen",
            "resolution",
            "processor",
            "camera",
            "zoom",
            "cell",
            "about",
            "is_favourite",
            "in_cart"
        )

