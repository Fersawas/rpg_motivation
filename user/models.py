from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator

from contants import USER_LENGTH, NAME_LENGHT, PASSWORD_LENGTH


class UserMain(AbstractUser):
    
    username = models.CharField(
        verbose_name='Логин',
        max_length=USER_LENGTH,
        validators=[RegexValidator(
            regex=r'[\w@+-]+', message='Недопустимые символы')]
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        validators=[EmailValidator(
            message='Неопустимый email'
        )])
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=NAME_LENGHT
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=NAME_LENGHT
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=PASSWORD_LENGTH
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


