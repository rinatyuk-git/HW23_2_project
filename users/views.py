import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтвердите адрес электронной почты',
            message=f'Просим перейти по ссылке {url} для подтверждения',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


# class Pass_recovery():
#     pass


class PasswordRecoveryView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/password_update.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        if user:
            # password = User.objects.make_random_password()
            # password = User.objects.make_password(password, salt=None, hasher='default')
            password = make_password('password', hasher='default')
            send_mail(
                    subject='Получите новый пароль к сайту',
                    message=f'Для входа на сайт используйте пароль: {password}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )
            user.set_password(password)
            user.save()
            return redirect(reverse('users:login'))
        return redirect(reverse('users/password_update.html'))
"""
Восстановление пароля зарегистрированного пользователя на автоматически
сгенерированный пароль.
Создайте новый контроллер для восстановления пароля.
Пароль можно сгенерировать с помощью библиотеки random.
Помните, что пароль в базе данных хранится в захешированном виде.
Для установки пароля пользователю можно воспользоваться функцией 
make_password()

"""
