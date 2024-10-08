# Generated by Django 5.1 on 2024-08-20 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_product_manufactured_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Признак публикации"),
        ),
        migrations.AlterField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                default=datetime.date(2024, 8, 20),
                help_text="Задайте дату производства продукта",
                verbose_name="Дата производства продукта",
            ),
        ),
    ]
