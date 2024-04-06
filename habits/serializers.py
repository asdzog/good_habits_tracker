from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitAwardValidator, ActionTimeValidator, RepeatValidator, PleasantHabitValidator, \
    RelatedHabitValidator


class HabitSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitAwardValidator(award_field='award', is_pleasant_field='is_pleasant'),
            ActionTimeValidator(time_field='duration'),
            RepeatValidator(days_field='days_between_repeat'),
            PleasantHabitValidator(is_pleasant_field='is_pleasant',
                                   award_field='award', related_field='related_habit'),
            RelatedHabitValidator(related_field='related_habit'),
        ]
