from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, PublicHabitListAPIView, PrivateHabitListAPIView, HabitRUDAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('habits/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habits/public/', PublicHabitListAPIView.as_view(), name='public_habits'),
    path('habits/private/', PrivateHabitListAPIView.as_view(), name='private_habits'),
    path('habits/<int:pk>/', HabitRUDAPIView.as_view(), name='habit-view'),
]
