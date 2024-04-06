import requests
from django.conf import settings
from habits.models import Habit


def send_telegram_notification(habit: Habit):

    user = habit.user
    user_name = [item for item in (
        user.first_name,
        user.last_name
    ) if item is not None]

    name = ' '.join(user_name) if user_name else user.email
    text = (f'Привет, {name}! Напоминаю, что сегодня, {habit.place},'
            f'в {habit.scheduled_time}, вы запланировали {habit.action}')

    requests.post(
        url=f'https://api.telegram.org/bot{settings.TG_TOKEN}/sendMessage',
        data={
            'chat_id': user.telegram_chat_id,
            'text': text,
        }
    )
