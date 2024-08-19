from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    validate_time_habit,
    validate_positive,
    RewardValidator,
    PleasantHabitValidator,
)
from users.serializer import UserSerializer


class HabitSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    time = IntegerField(validators=[validate_time_habit])
    time_to_complete = IntegerField(validators=[validate_positive])

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardValidator(fields=["reward", "related_habit"]),
            PleasantHabitValidator(field="sign_pleasant_habit"),
        ]
