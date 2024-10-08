# Generated by Django 5.1 on 2024-08-26 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                default=datetime.date(2024, 8, 26),
                help_text="Задайте дату производства продукта",
                verbose_name="Дата производства продукта",
            ),
        ),
    ]
