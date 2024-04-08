from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    scheduled_time = models.TimeField(verbose_name='время дня для выполнения', db_index=True)
    place = models.CharField(max_length=64, verbose_name='место')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='является приятной')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      **NULLABLE, verbose_name='связанная привычка')
    days_between_repeat = models.PositiveIntegerField(default=1, verbose_name='дней между повторами')
    award = models.CharField(max_length=100, **NULLABLE, verbose_name='награда')
    duration = models.PositiveIntegerField(default=120, verbose_name='длительность, сек')
    is_public = models.BooleanField(default=False, verbose_name='является публичной')

    def __str__(self):
        return f'{self.action} в {self.scheduled_time}, место: {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
