from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from habits.models import Habit


@shared_task
def send_reminder(habit: Habit):
    """ Send email to user when the course is updated """

    habits = Habit.objects.all().filter()
    users = [habit.user for habit in habits]
    for user in users:
        for habit in habits:
            send_mail(
                subject="Уведомление о выполнении привычки",
                message=f"Материалы курса {str(habit.action)} были обновлены.",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )