import os
import uuid

from django.db import models

from device.models import Device
from django.utils.text import slugify


class Phone(Device):
    cell = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


def phone_image_file_path(instance, filename: str):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads", "phones", filename)


class Image(models.Model):
    name = models.CharField(max_length=255)
    phones = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="images", null=True)
    url = models.ImageField(upload_to=phone_image_file_path, null=True)

    def __str__(self) -> str:
        return self.name
