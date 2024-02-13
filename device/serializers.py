from rest_framework import serializers
from .models import Memory, Color, Device


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ("id", "ram", "capacity", "price")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name", "hex_value")


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
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
            "about"
        )


class DeviceListSerializer(DeviceSerializer):
    memories = MemorySerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ("id", "name", "screen", "memories")


class DeviceDetailSerializer(DeviceListSerializer):
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Device
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
            "about",
        )
