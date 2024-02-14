from django.db import models

from device.models import Device


class Phone(Device):
    zoom = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
