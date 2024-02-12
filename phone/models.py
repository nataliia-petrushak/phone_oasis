from django.db import models


class Memory(models.Model):
    ram = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex_value = models.CharField(max_length=255, blank=True, null=True)


class Image(models.Model):
    url = models.URLField()


class Phone(models.Model):
    name = models.CharField(max_length=255)
    memories = models.ManyToManyField(Memory, related_name="phones")
    colors = models.ManyToManyField(Color, related_name="phones")
    screen = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    zoom = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    about = models.TextField()
    is_favourite = models.BooleanField(default=False)
    in_cart = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
