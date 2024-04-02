from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None

    first_name = models.CharField(max_length=32, **NULLABLE, verbose_name='имя')
    last_name = models.CharField(max_length=64, **NULLABLE, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    is_active = models.BooleanField(default=False, verbose_name='активен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
