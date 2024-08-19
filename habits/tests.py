from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from habits.models import Habit
from habits.serializer import HabitSerializer

class HabitApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')
        self.habit_data = {
            'time': 10,
            'place': 'Home',
            'action': 'Read a book',
            'sign_pleasant_habit': False,
            'periodicity': 'every_day',
            'time_to_complete': 60,
            'public': True
        }
        self.habit = Habit.objects.create(user=self.user, **self.habit_data)

    def test_create_habit(self):
        url = reverse('habits:habits_create')
        response = self.client.post(url, self.habit_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertEqual(Habit.objects.last().user, self.user)

    # def test_update_habit(self):
    #     url = reverse('habits:habits_update', kwargs={'pk': self.habit.pk})
    #     updated_data = {'action': 'Read a newspaper'}
    #     response = self.client.put(url, updated_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.habit.refresh_from_db()
    #     self.assertEqual(self.habit.action, 'Read a newspaper')
    #
    # def test_retrieve_habit(self):
    #     url = reverse('habits:habits_retrieve', kwargs={'pk': self.habit.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['action'], 'Read a book')
    #
    # def test_delete_habit(self):
    #     url = reverse('habits:habits_delete', kwargs={'pk': self.habit.pk})
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Habit.objects.count(), 0)
    #
    # def test_list_habits(self):
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['results']), 1)
    #
    # def test_list_habits_as_staff(self):
    #     self.user.is_staff = True
    #     self.user.save()
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['results']), 1)
    #
    # def test_list_habits_as_non_staff(self):
    #     self.user.is_staff = False
    #     self.user.save()
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['results']), 1)
    #
    # def test_list_habits_public_only(self):
    #     self.habit.public = False
    #     self.habit.save()
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['results']), 0)
    #
    # def test_list_habits_owned_by_user(self):
    #     self.habit.public = False
    #     self.habit.save()
    #     url = reverse('habits:habits_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['results']), 1)
    #
    # def test_permissions(self):
    #     self.client.logout()
    #     url = reverse('habits:habits_retrieve', kwargs={'pk': self.habit.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    #     self.client.login(email='testuser@example.com', password='testpassword')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
