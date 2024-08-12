from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitRetrieveApiView,
                          HabitUpdateApiView)

app_name = HabitsConfig.name
urlpatterns = [
    path("create/", HabitCreateApiView().as_view(), name="habits_create"),
    path("update/", HabitUpdateApiView().as_view(), name="habits_update"),
    path("detail/", HabitRetrieveApiView().as_view(), name="habits_retrieve"),
    path("list/", HabitListApiView().as_view(), name="habits_list"),
    path("delete/", HabitDestroyApiView().as_view(), name="habits_delete"),
]
