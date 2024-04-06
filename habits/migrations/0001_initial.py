# Generated by Django 4.2.7 on 2024-04-04 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.TimeField(verbose_name='время дня для выполнения')),
                ('place', models.CharField(blank=True, max_length=64, null=True, verbose_name='место')),
                ('action', models.CharField(blank=True, max_length=100, null=True, verbose_name='действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='является приятной')),
                ('days_between_repeat', models.PositiveIntegerField(default=1, verbose_name='дней между повторами')),
                ('award', models.CharField(blank=True, max_length=100, null=True, verbose_name='награда')),
                ('duration', models.PositiveIntegerField(default=120, verbose_name='длительность, сек')),
                ('is_public', models.BooleanField(default=False, verbose_name='является публичной')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
