from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from users.models import User
from users.serializer import UserSerializer


class HabitsSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
