from django.core.exceptions import ValidationError


def validate_positive(value):
    if value >= 120 or value < 0:
        raise ValidationError(f"Время на привычку не должно быть больше 120 сек.")


def validate_time_habit(value):
    if value >= 23 or value < 0:
        raise ValidationError(f"Время для выполнения привычки должно быть не более 23")
