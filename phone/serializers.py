from rest_framework import serializers
from .models import Phone, Image
from device.serializers import DeviceSerializer, DeviceListSerializer, DeviceDetailSerializer


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("url",)


class PhoneSerializer(DeviceSerializer):
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


class PhoneListSerializer(DeviceListSerializer):
    images = ImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Phone
        fields = ("id", "name", "screen", "memories", "images")


class PhoneDetailSerializer(DeviceDetailSerializer):
    images = ImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Phone
        fields = "__all__"

