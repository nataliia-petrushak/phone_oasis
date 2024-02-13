from django.db import models


class Memory(models.Model):
    ram = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "memories"

    def __str__(self) -> str:
        return f"{self.ram}, {self.capacity} -> {self.price}"


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.hex_value}"


class Device(models.Model):
    name = models.CharField(max_length=255)
    memories = models.ManyToManyField(Memory)
    colors = models.ManyToManyField(Color)
    screen = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    zoom = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self) -> str:
        return self.name
