from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from character.tasks import create_character_task, create_character_equipment_task

from character.models import Character


User = get_user_model()

@receiver(post_save, sender=User)
def create_character(sender, instance, created, **kwargs):
    if created:
        create_character_task.delay(instance.id)

@receiver(post_save, sender=Character)
def create_character_equipment(sender, instance, created, **kwargs):
    if created:
        create_character_equipment_task(instance.id)