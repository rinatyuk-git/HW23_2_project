from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "product_price",
        "category",
    )
    # продуктов выведите в список id, название, цену и категорию.
    list_filter = ("category",)
    # результат отображения фильтровать по категории
    search_fields = (
        "product_name",
        "product_info",
    )


# осуществлять поиск по названию и полю описания.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category_name",
    )


# Для категорий выведите id и наименование в список отображения


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "version_name",
        "version_number",
        "product_name",
        "is_actual",
    )
    list_filter = (
        "version_name",
        "product_name",
    )
    search_fields = (
        "version_name",
        "version_number",
    )


# admin.site.register(Product)
# Register your models here.
