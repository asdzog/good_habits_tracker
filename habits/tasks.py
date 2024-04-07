from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from habits.services import send_telegram_notification
from habits.models import Habit


@shared_task
def send_reminder():
    """ Send message to user 10 minutes before the habit scheduled time """
    now = timezone.now()

    qs = Habit.objects.filter(
        scheduled_time__gte=now + timedelta(minutes=2),
        scheduled_time__le=now + timedelta(minutes=3),
    )
    qs = qs.select_related('user').filter(
        user__telegram_chat_id__isnull=False
    )

    for habit in qs:
        send_telegram_notification(habit)
