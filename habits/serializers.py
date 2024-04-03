from rest_framework import serializers

from habits.models import Habit, PleasantHabit
from habits.validators import HabitAwardValidator, ActionTimeValidator, RepeatValidator


class PleasantHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = PleasantHabit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitAwardValidator(award_field='award', is_pleasant_field='is_pleasant'),
            ActionTimeValidator(time_field='duration'),
            RepeatValidator(days_field='days_between_repeat'),
        ]
