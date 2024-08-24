from django.core.exceptions import ValidationError




def validate_positive(value):
    if value >= 120 or value < 0:
        raise ValidationError(f"Время на привычку не должно быть больше 120 сек.")


def validate_time_habit(value):
    if value >= 23 or value < 0:
        raise ValidationError(f"Время для выполнения привычки должно быть не более 23")


class RewardValidator:
    def __init__(self, fields):
        self.reward = fields[0]
        self.related_habit = fields[1]

    def __call__(self, value):
        reward = value.get(self.reward)
        related_habit = value.get(self.related_habit)

        if reward and related_habit:
            raise ValidationError("Нельзя указать и награду, и приятную привычку.")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field):
            if value.get("reward") or value.get("related_habit"):
                raise ValidationError(
                    "Нельзя указать награду и связанную  привычку для приятной привычки"
                )


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        baba = self.field

        print(value.getattr("related_habit"))
