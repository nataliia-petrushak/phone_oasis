from rest_framework import serializers
from .models import Phone
from device.serializers import DeviceSerializer, DeviceListSerializer, DeviceDetailSerializer


class PhoneSerializer(DeviceSerializer):
    class Meta:
        model = Phone
        fields = (
            "id",
            "name",
            "category",
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

    class Meta:
        model = Phone
        fields = ("id", "name", "category", "images", "screen", "memories")


class PhoneDetailSerializer(DeviceDetailSerializer):

    class Meta:
        model = Phone
        fields = "__all__"

