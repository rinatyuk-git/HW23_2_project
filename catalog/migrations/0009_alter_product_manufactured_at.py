# Generated by Django 5.1 on 2024-08-18 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_product_owner_alter_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                default=datetime.date(2024, 8, 18),
                help_text="Задайте дату производства продукта",
                verbose_name="Дата производства продукта",
            ),
        ),
    ]
