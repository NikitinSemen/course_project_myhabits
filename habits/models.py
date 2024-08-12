from django.db import models

from users.models import User


class Habit(models.Model):
    PERIODICITY_CHOICES = [
        ('every_day', 'каждый день'),
        ('every_other_day', 'через день'),
        ('every_two_days', 'раз в два дня'),
        ('once_a_week', 'раз в неделю'),
    ]
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    place = models.CharField(max_length=200, verbose_name='Место')
    action = models.CharField(max_length=200, verbose_name='Действие')
    sign_pleasant_habit = models.BooleanField(verbose_name='признак приятной привычки', default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES, default='every_day',
                                   verbose_name='Периодичность')
    reward = models.CharField(verbose_name='Вознаграждение', null=True, blank=True)
    time_to_complete = models.PositiveSmallIntegerField(verbose_name='время на выполнение привычки', default=120)
    public = models.BooleanField(verbose_name='Публичность привычки', default=False)

    def __str__(self):
        return f'Я буду {self.action} {self.periodicity} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural= 'Привычка'
