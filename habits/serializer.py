from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from users.serializer import UserSerializer


class HabitSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        reward = attrs.get("reward")
        related_habit = attrs.get("related_habit")
        if reward and related_habit is not None:
            raise ValidationError(
                "Необходимо заполнить или Вознаграждение за привычку или приятную привычку"
            )
        if attrs.get("sign_pleasant_habit"):
            if (
                attrs.get("reward") is not None
                or attrs.get("related_habit") is not None
            ):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждений или приятной привычки"
                )

        return attrs
