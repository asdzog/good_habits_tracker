from django.contrib import admin

from habits.models import Habit, PleasantHabit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'place', 'is_pleasant', 'user')
    list_filter = ('action', 'user', 'is_pleasant', 'place', )


@admin.register(PleasantHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'place', 'is_pleasant', 'user')
    list_filter = ('action', 'user', 'is_pleasant', 'place', )
