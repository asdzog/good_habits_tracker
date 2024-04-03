from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, PublicHabitListAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitDetailsAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('create_habit/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits'),
    path('habit/<int:pk>/', HabitDetailsAPIView.as_view(), name='get_habit'),
    path('update_habit/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete_habit/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete_habit'),
]
