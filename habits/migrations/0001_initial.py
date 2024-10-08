# Generated by Django 5.0.8 on 2024-08-13 11:02

import django.db.models.deletion
import habits.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.PositiveSmallIntegerField(
                        validators=[habits.validators.validate_time_habit],
                        verbose_name="Время",
                    ),
                ),
                ("place", models.CharField(max_length=200, verbose_name="Место")),
                ("action", models.CharField(max_length=200, verbose_name="Действие")),
                (
                    "sign_pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("every_day", "каждый день"),
                            ("every_other_day", "через день"),
                            ("every_two_days", "раз в два дня"),
                            ("once_a_week", "раз в неделю"),
                        ],
                        default="every_day",
                        max_length=20,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, null=True, verbose_name="Вознаграждение"
                    ),
                ),
                (
                    "time_to_complete",
                    models.PositiveSmallIntegerField(
                        default=120,
                        validators=[habits.validators.validate_positive],
                        verbose_name="время на выполнение привычки",
                    ),
                ),
                (
                    "public",
                    models.BooleanField(
                        default=False, verbose_name="Публичность привычки"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычка",
            },
        ),
    ]
