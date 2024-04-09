from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from config.celery import app
from habits.services import send_telegram_notification
from habits.models import Habit


@shared_task
def send_reminder():
    """ Send message to user 10 minutes before the habit scheduled time """
    now = timezone.datetime.now()

    ten_minutes_later = now + timedelta(minutes=10)
    eleven_minutes_later = now + timedelta(minutes=11)

    qs = Habit.objects.filter(
        scheduled_time__gte=ten_minutes_later.time(),
        scheduled_time__lt=eleven_minutes_later.time()
    )
    qs = qs.select_related('user').exclude(
        user__telegram_chat_id__isnull=True
    )

    for habit in qs:
        send_telegram_notification_task.delay(habit.id)


@app.task()
def send_telegram_notification_task(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    send_telegram_notification(habit)
