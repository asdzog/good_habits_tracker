from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import HabitsPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitsPagination

    def get_queryset(self):
        queryset = Habit.objects.all()
        return queryset.filter(is_public=True)


class PrivateHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPagination

    def get_queryset(self):
        queryset = Habit.objects.all()
        return queryset.filter(user=self.request.user, is_public=False)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
