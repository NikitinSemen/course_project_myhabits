from rest_framework import generics

from .models import Habit
from .pagination import CustomPagination
from .serializer import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyApiView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user and user.is_staff:
            return Habit.objects.all()
        return Habit.objects.filter(public=True) | Habit.objects.filter(user=user)
