from device.views import DeviceViewSet

from .models import Tablet
from .serializers import TabletSerializer, TabletListSerializer, TabletDetailSerializer


class TabletViewSet(DeviceViewSet):
    queryset = Tablet.objects.prefetch_related("colors", "memories", "images").select_related("category")
    serializer_class = TabletSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TabletListSerializer
        if self.action == "retrieve":
            return TabletDetailSerializer
        return self.serializer_class
