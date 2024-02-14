from device.views import DeviceViewSet

from .models import Phone
from .serializers import PhoneSerializer, PhoneListSerializer, PhoneDetailSerializer


class PhoneViewSet(DeviceViewSet):
    queryset = Phone.objects.prefetch_related("colors", "memories", "images").select_related("category")
    serializer_class = PhoneSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PhoneListSerializer
        if self.action == "retrieve":
            return PhoneDetailSerializer
        return self.serializer_class
