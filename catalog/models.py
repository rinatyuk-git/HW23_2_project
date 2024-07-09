from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )  # Наименование
    category_info = models.TextField(
        max_length=1255,
        verbose_name="Информация о категории",
        help_text="Введите информацию о категории",
    )  # Описание

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )  # Наименование
    product_info = models.TextField(
        max_length=1255,
        verbose_name="Информация о продукте",
        help_text="Введите информацию о продукте",
    )  # Описание
    product_image = models.ImageField(
        upload_to="product/images",
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
        **NULLABLE
    )  # Изображение (превью)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name='products',
        **NULLABLE
    )  # pass # Категория
    product_price = models.DecimalField  # Цена за покупку
    created_at = models.DateField  # Дата создания (записи в БД)
    updated_at = models.DateField  # Дата последнего изменения (записи в БД)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        # ordering = ('name',)

    def __str__(self):
        return self.name



# Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».
# У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.
# Воспользуйтесь специальным полем модели — ForeignKey().
# При необходимости подробнее про то, как работает такое поле, можно почитать тут.
# Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия — created_at и updated_at соответственно.
