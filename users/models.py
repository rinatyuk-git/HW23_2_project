from django.contrib.auth.models import AbstractUser
from django.db import models


"""
Создайте новое приложения для работы с пользователем.
Определите собственную модель для пользователя, при этом
задайте электронную почту как поле для авторизации.

"""


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Почтовый адрес',
        unique=True,
    )

    phone = models.CharField(
        max_length=35,
        verbose_name='Номер телефона',
        blank=True,
        null=True,
    ) # номер телефона,
    avatar = models.ImageField(
        upload_to="users/images",
        verbose_name="Аватар пользователя",
        help_text="Загрузите аватар пользователя",
        blank=True,
        null=True,
    )  # аватар,
    country = models.CharField(
        max_length=55,
        verbose_name='Страна',
        blank=True,
        null=True,
    ) # страна,
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []