import requests
from rest_framework.exceptions import ValidationError
from django.conf import settings


class ChatIDValidator:

    def __init__(self, chat_id_field):
        self.chat_id = chat_id_field

    def __call__(self, value):
        chat_id = dict(value).get(self.chat_id)
        if chat_id:
            url = f'https://api.telegram.org/bot{settings.TG_TOKEN}/getChat?chat_id={chat_id}'
            response = requests.get(url)
            data = response.json()
            data_ok = 'ok' in data and data['ok']
            result_valid = 'result' in data and 'type' in data['result'] and data['result']['type'] == 'private'
            if not (data_ok and result_valid):
                raise ValidationError('Указанный Telegram Chat ID некорректный. '
                                      'Если вы уверены в его правильности, убедитесь, '
                                      'что TG_TOKEN указан в настройках верно')
