from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('create_habit/', HabitCreateAPIView.as_view(), name='create_habit'),
]
