from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwnerOrReadOnly
from .models import Habit
from .pagination import CustomPagination
from .serializer import HabitSerializer
from .tasks import add_habit_to_schedule


class HabitCreateApiView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        add_habit_to_schedule(habit.id)


class HabitUpdateApiView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_update(self, serializer):
        habit = serializer.save()
        add_habit_to_schedule(habit.id)


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """Детали привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)


class HabitDestroyApiView(generics.DestroyAPIView):
    """Удаление привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class HabitListApiView(generics.ListAPIView):
    """Просмотр всех привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        user = self.request.user
        if user and user.is_staff:
            return Habit.objects.all()
        return Habit.objects.filter(public=True) | Habit.objects.filter(user=user)


class HabitIsPublicListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(public=True)
    pagination_class = CustomPagination
