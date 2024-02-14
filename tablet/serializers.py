from .models import Tablet
from device.serializers import DeviceSerializer, DeviceListSerializer, DeviceDetailSerializer


class TabletSerializer(DeviceSerializer):
    class Meta:
        model = Tablet
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
            "about"
        )


class TabletListSerializer(DeviceListSerializer):

    class Meta:
        model = Tablet
        fields = ("id", "name", "category", "images", "screen", "memories")


class TabletDetailSerializer(DeviceDetailSerializer):

    class Meta:
        model = Tablet
        fields = "__all__"
