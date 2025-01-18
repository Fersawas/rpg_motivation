from django.db import models
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

from contants import (CHAR_EQUIP, FIELD_OPTION, DEF_POINTS_CHAR,
                      DEF_POINTS_EQ, EQUIP_LENGTH, EQUIP_TYPE_LENGTH)


User = get_user_model()


class Equipment(models.Model):
    EQUIP_CHOICES = [
        ('H', 'Hands'),
        ('C', 'Chest'),
        ('L', 'Legs'),
        ('W', 'Weapon')
    ]

    title = models.CharField(verbose_name='Название', max_length=EQUIP_LENGTH)
    description = models.CharField(verbose_name='Описание', max_length=EQUIP_LENGTH)
    type = models.CharField(verbose_name='Тип', max_length=EQUIP_TYPE_LENGTH, choices=EQUIP_CHOICES)
    
    bonus_strenght = models.IntegerField(verbose_name='Дополниткльная сила', default=DEF_POINTS_EQ)
    bonus_intelegence = models.IntegerField(verbose_name='Дополнительный интеллект', default=DEF_POINTS_EQ)
    bonus_agility = models.IntegerField(verbose_name='Доплнительная ловкость', default=DEF_POINTS_EQ)
    bonus_wisdom = models.IntegerField(verbose_name='Дополнительная мудрость', default=DEF_POINTS_EQ)



class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='character')
    strenght = models.IntegerField(default=DEF_POINTS_CHAR)
    intelegence = models.IntegerField(default=DEF_POINTS_CHAR)
    agility = models.IntegerField(default=DEF_POINTS_CHAR)
    wisdom = models.IntegerField(default=DEF_POINTS_CHAR)


class CharacterEquipment(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE,
                                     related_name='char_equipment', **FIELD_OPTION)
    hands = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                 related_name='char_eq_hands', **FIELD_OPTION)
    chest = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                 related_name='char_eq_chest', **FIELD_OPTION)
    legs = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                related_name='char_eq_legs', **FIELD_OPTION)
    weapon = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                  related_name='char_eq_weap', **FIELD_OPTION) 
    
    def clean(self) -> None:
        if self.hands and self.hands.type != 'H':
            raise ValidationError(message={
                'ERROR': CHAR_EQUIP['hands']
            })
        
        if self.chest and self.chest.type != 'C':
            raise ValidationError(message={
                'ERROR': CHAR_EQUIP['chest']
            })

        if self.legs and self.legs.type != 'L':
            raise ValidationError(message={
                'ERROR': CHAR_EQUIP['legs']
            })
        
        if self.weapon and self.weapon.type != 'W':
            raise ValidationError(message={
                'ERROR': CHAR_EQUIP['weapon']
            })
    
    def save(self, *args, **kwargs):
        self.clean()
        super(CharacterEquipment, self).save(*args, **kwargs)