from celery import shared_task
from celery.schedules import crontab

from config.celery import app
from .models import Habit
from .services import send_telegram_message


@shared_task
def send_message_telegram(user_tg_id, habit_action, habit_place, habit_time):
    message = (
        f"Привет!\nТы просил напомнить о твоей новой привычке\n я буду {habit_action} в "
        f"{habit_time}часов в {habit_place}"
    )
    send_telegram_message(message, user_tg_id)


def add_habit_to_schedule(habit_id):
    habit = Habit.objects.get(id=habit_id)
    user_tg_id = habit.user.tg_id
    habit_action = habit.action
    habit_place = habit.place
    habit_time = habit.time

    schedule = None

    if habit.periodicity == "every_day":
        schedule = crontab(minute="*")
    elif habit.periodicity == "every_other_day":
        schedule = crontab(minute="0", hour=f"{habit.time}", day_of_month="*/2")
    elif habit.periodicity == "every_two_days":
        schedule = crontab(minute="0", hour=f"{habit.time}", day_of_month="*/3")
    elif habit.periodicity == "once_a_week":
        schedule = crontab(minute="0", hour=f"{habit.time}", day_of_week="sun")

    if schedule:
        app.conf.beat_schedule[f"habit-{habit_id}"] = {
            "task": "habits.tasks.send_message_telegram",
            "schedule": schedule,
            "args": (user_tg_id, habit_action, habit_place, habit_time),
        }
        app.loader.import_default_modules()
