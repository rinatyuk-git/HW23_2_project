# Generated by Django 5.0.6 on 2024-08-07 10:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                default=datetime.date(2024, 8, 7),
                help_text="Задайте дату производства продукта",
                verbose_name="Дата производства продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                blank=True,
                help_text="Введите название продукта",
                max_length=100,
                null=True,
                unique=True,
                verbose_name="Название продукта",
            ),
        ),
        migrations.CreateModel(
            name="Version",
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
                (
                    "version_number",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Задайте номер версии",
                        max_digits=10,
                        verbose_name="Номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        help_text="Введите название версии",
                        max_length=100,
                        unique=True,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_actual",
                    models.BooleanField(
                        default=True, verbose_name="Признак текущей версии"
                    ),
                ),
                (
                    "product_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="Название продукта",
                    ),
                ),
            ],
        ),
    ]
