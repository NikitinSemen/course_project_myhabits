from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    validate_time_habit,
    validate_positive,
    RewardValidator,
    PleasantHabitValidator, RelatedHabitValidator,
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
            RelatedHabitValidator(field="related_habit")
        ]

    def validate(self, data):
        if data.get('related_habit'):
            habit = Habit.objects.get(pk=data.get('related_habit').pk)
            if not habit.pleasant_habit:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                      'привычки')

        return data
