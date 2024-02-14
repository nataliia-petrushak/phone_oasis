import os
import uuid

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.hex_value}"


def devices_image_file_path(instance, filename: str):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.device_name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads", instance.color.name, instance.product_category.name, filename)


class Image(models.Model):
    device_name = models.CharField(max_length=255)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.ImageField(upload_to=devices_image_file_path, null=True)

    def __str__(self) -> str:
        return f"{self.device_name} - {self.color.name}"


class Memory(models.Model):
    ram = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    new_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
        verbose_name_plural = "memories"

    def __str__(self) -> str:
        return f"{self.ram}, {self.capacity} -> {self.price}"


class Device(models.Model):
    name = models.CharField(max_length=255)
    images = models.ManyToManyField(Image)
    memories = models.ManyToManyField(Memory)
    colors = models.ManyToManyField(Color)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    screen = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    year_of_creation = models.IntegerField(null=True)
    about = models.TextField()

    def __str__(self) -> str:
        return self.name
