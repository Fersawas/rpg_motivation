from django.db import models
from django.contrib.auth import get_user_model

from contants import (NAME_LENGHT, DESCRIPTION_LENGTH,
                      FIELD_OPTION, BONUS_POWER_LENGTH, STATUS_LENGTH)


User = get_user_model()


class Quest(models.Model):
    POWER_CHOICES = [
    ('S', 'strenght'),
    ('I', 'intelegence'),
    ('A', 'agility'),
    ('W', 'Wisdom')
    ]

    title = models.CharField(verbose_name='Название',
                             max_length=NAME_LENGHT)
    description = models.CharField(verbose_name='Описание',
                                   max_length=DESCRIPTION_LENGTH)
    task_time = models.DurationField(verbose_name='Время выполнения квеста')
    bonus_power_points = models.IntegerField(verbose_name='Очки за квест', default=0)
    bonus_power = models.CharField(verbose_name='Повышенная характеристика',
                                   max_length=BONUS_POWER_LENGTH, choices=POWER_CHOICES)
    user = models.ManyToManyField(User, related_name='user_quest', through='UserQuest')


class UserQuest(models.Model):
    STATUS_CHOICES = [
        ('A', 'active'),
        ('C', 'completed'),
        ('F', 'failed'),
        ('N', 'not started')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, verbose_name='Квест')
    start_quest_time = models.DateTimeField(verbose_name='Время начала квеста', **FIELD_OPTION)
    end_quest_time = models.DateTimeField(verbose_name='Время окончания квеста', **FIELD_OPTION)
    status = models.CharField(verbose_name='Статус квеста', choices=STATUS_CHOICES, max_length=STATUS_LENGTH, default='N')
