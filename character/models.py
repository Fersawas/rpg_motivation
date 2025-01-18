from django.db import models
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

from contants import CHAR_EQUIP


User = get_user_model()


class Equipment(models.Model):
    EQUIP_CHOICES = [
        ('H', 'Hands'),
        ('C', 'Chest'),
        ('L', 'Legs'),
        ('W', 'Weapon')
    ]

    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    type = models.CharField(verbose_name='Тип', max_length=50, choices=EQUIP_CHOICES)
    
    bonus_strenght = models.IntegerField(verbose_name='Дополниткльная сила', default=0)
    bonus_intelegence = models.IntegerField(verbose_name='Дополнительный интеллект', default=0)
    bonus_agility = models.IntegerField(verbose_name='Доплнительная ловкость', default=0)
    bonus_wisdom = models.IntegerField(verbose_name='Дополнительная мудрость', default=0)



class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='character')
    strenght = models.IntegerField(default=5)
    intelegence = models.IntegerField(default=5)
    agility = models.IntegerField(default=5)
    wisdom = models.IntegerField(default=5)


class CharacterEquipment(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE,
                                     related_name='char_equipment', null=True, blank=True)
    hands = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                 related_name='char_eq_hands', null=True, blank=True)
    chest = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                 related_name='char_eq_chest', null=True, blank=True)
    legs = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                related_name='char_eq_legs', null=True, blank=True)
    weapon = models.OneToOneField(Equipment, on_delete=models.CASCADE,
                                  related_name='char_eq_weap', null=True, blank=True) 
    
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