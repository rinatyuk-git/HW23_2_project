from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                "product_name": "Сок клубничный",
                "product_info": "Свежевыжатый",
                "product_price": '15.95'
            },
            {
                "product_name": "Водка Nemiroff DeLuxe",
                "product_info": "Эххх, хороша!!!",
                "product_price": "259.54",
            },
            {
                "product_name": "Бананы",
                "product_info": "Эквадор - страна бананная!!!",
                "product_price": "25.89",
            },
            {
                "product_name": "Картофель",
                "product_info": "Где картошка - там и рыбка, а где рыбка - там и выпить не грех!!!",
                "product_price": "18.06",
            },
            {
                "product_name": "Лимонад Сидр типа",
                "product_info": "Пшшшш!!!! И много, много, много бубликов!!!",
                "product_price": "65.89",
            },
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)


        category_list = [
            {"category_name": "Овощи", "category_info": "Вкусные"},
            {"category_name": "Фрукты", "category_info": "Свежие с грядки"},
            {"category_name": "Алкоголь", "category_info": "Крепкий"},
            {"category_name": "Напитки", "category_info": "Газированные с шариками"},
            {"category_name": "Соки", "category_info": "Разные, вкусные"},
        ]

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
