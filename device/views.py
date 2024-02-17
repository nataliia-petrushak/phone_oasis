from abc import ABC

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet, ABC):
    queryset = Device.objects.prefetch_related("images", "colors", "memories").select_related("categories")
    serializer_class = DeviceSerializer

    def get_queryset(self):

        """All the devices will be ordered by the year of creation:
        from the newest to the oldest"""

        self.queryset = self.queryset.order_by("-year_of_creation")

        device_name = self.request.query_params.get("name")

        if device_name:
            self.queryset = self.queryset.filter(name__icontains=device_name)

        return self.queryset

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name="name",
                type=OpenApiTypes.STR,
                description="Filter devices by "
                            "the name (ex. ?name=Apple iPhone 15 Pro Max)"
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
