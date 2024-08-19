from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateApiView,
    HabitDestroyApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
)

app_name = HabitsConfig.name
urlpatterns = [
    path("create/", HabitCreateApiView.as_view(), name="habits_create"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="habits_update"),
    path("detail/<int:pk>/", HabitRetrieveApiView.as_view(), name="habits_retrieve"),
    path("list/", HabitListApiView.as_view(), name="habits_list"),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habits_delete"),
]
