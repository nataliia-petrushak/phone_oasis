# Generated by Django 5.0.2 on 2024-02-12 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("hex_value", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Memory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ram", models.CharField(max_length=255)),
                ("capacity", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("screen", models.CharField(max_length=255)),
                ("resolution", models.CharField(max_length=255)),
                ("processor", models.CharField(max_length=255)),
                ("camera", models.CharField(max_length=255)),
                ("zoom", models.CharField(max_length=255)),
                ("cell", models.CharField(max_length=255)),
                ("about", models.TextField()),
                ("is_favourite", models.BooleanField(default=False)),
                ("in_cart", models.BooleanField(default=False)),
                (
                    "colors",
                    models.ManyToManyField(related_name="phones", to="phone.color"),
                ),
                (
                    "images",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="phone.image"
                    ),
                ),
                (
                    "memories",
                    models.ManyToManyField(related_name="phones", to="phone.memory"),
                ),
            ],
        ),
    ]
