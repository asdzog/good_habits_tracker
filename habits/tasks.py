from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from habits.services import send_telegram_notification
from habits.models import Habit


@shared_task
def send_reminder():
    """ Send message to user  15 minutes before the habit scheduled time """
    current_time = timezone.now().time()
    reminder_time = current_time + timedelta(minutes=15)
    habits = Habit.objects.all().filter()
    for habit in habits:
        if habit.scheduled_time <= reminder_time:
            send_telegram_notification(habit)
