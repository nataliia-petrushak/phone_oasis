from abc import ABC

from rest_framework import viewsets
from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet, ABC):
    queryset = Device.objects.prefetch_related("images", "colors", "memories").select_related("categories")
    serializer_class = DeviceSerializer

    def get_queryset(self):
        self.queryset = self.queryset.order_by("-year_of_creation")

        device_name = self.request.query_params.get("name")

        if device_name:
            self.queryset = self.queryset.filter(name__icontains=device_name)

        return self.queryset
