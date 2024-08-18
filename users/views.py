import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    # создаем регистрацию Пользователя
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        # Валидируем пользователя автоматической отправкой сообщения на ящик
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтвердите адрес электронной почты",
            message=f"Просим перейти по ссылке {url} для подтверждения",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    # Верифицируем пользователя по отправленному/полученному токену
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    # создаем профиль Пользователя с возможностью его изменения
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class PasswordRecoveryView(PasswordResetView):
    # создаем инструмент обновления пароля
    form_class = PasswordResetForm
    template_name = "users/password_update.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        # создание, валидация и верификация нового пароля
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        if user:
            password = secrets.token_urlsafe(17)
            send_mail(
                subject="Получите новый пароль к сайту",
                message=f"Для входа на сайт используйте пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            user.set_password(password)
            user.save()
            return redirect(reverse("users:login"))
        return redirect(reverse("users/password_update.html"))


"""
Пароль можно сгенерировать с помощью библиотеки random.
Помните, что пароль в базе данных хранится в захешированном виде.
Для установки пароля пользователю можно воспользоваться функцией
make_password()
"""
