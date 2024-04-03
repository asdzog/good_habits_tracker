from rest_framework.exceptions import ValidationError


class HabitAwardValidator:

    def __init__(self, award_field, is_pleasant_field):
        self.award = award_field
        self.is_pleasant = is_pleasant_field

    def __call__(self, value):
        if dict(value).get(self.award) and dict(value).get(self.is_pleasant):
            raise ValidationError('Можно выбрать только одно: или награду, или приятную привычку в виде вознаграждения.')


class ActionTimeValidator:

    def __init__(self, time_field):
        self.time = time_field

    def __call__(self, value):
        seconds = dict(value).get(self.time)
        if int(seconds) > 120:
            raise ValidationError(f"Длительность не может быть свыше двух минут (120 сек)."
                                  f"Сейчас указано значение {seconds} секунд.")


class RepeatValidator:

    def __init__(self, days_field):
        self.days = days_field

    def __call__(self, value):
        days = dict(value).get(self.days)
        if int(days) > 7:
            raise ValidationError(f"Периодичность не может быть свыше 7 дней."
                                  f"Сейчас указано значение {days} дней.")


class PleasantHabitValidator:

    def __init__(self, is_pleasant_field):
        self.is_pleasant = is_pleasant_field

    def __call__(self, value):
        if self.is_pleasant:
            raise ValidationError(f"Периодичность не может быть свыше 7 дней."
                                  f"Сейчас указано значение {days} дней.")

