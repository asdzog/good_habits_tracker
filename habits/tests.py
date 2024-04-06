from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@mail.com',
            password='test_psw',
            is_active=True
        )

        self.user.set_password(self.user.password)
        self.user.save()

        access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.habit = Habit.objects.create(
            user=self.user,
            scheduled_time='08:00:00',
            place='дома',
            action='отжаться 50 раз',
            award='выпить 0.5л кефира',
            duration=90,
            is_public=True,
        )

    def test_create_habit(self):
        """Test of creating a habit"""
        data = {
            'scheduled_time': '08:00:00',
            'action': 'отжаться 50 раз',
            'place': 'на улице',
            'award': 'выпить 0.5л кефира',
            'user': self.user
        }

        response = self.client.post(
            reverse('habits:create_habit'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        response_private_habits = self.client.get(
            reverse('habits:private_habits')
        )

        self.assertEqual(
            Habit.objects.all().filter(is_public=False).count(),
            response_private_habits.json()['count']
        )

        response_public_habits = self.client.get(
            reverse('habits:public_habits')
        )

        self.assertEqual(
            Habit.objects.all().filter(is_public=True).count(),
            response_public_habits.json()['count']
        )
