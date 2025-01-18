from django.contrib.auth import get_user_model

from celery import shared_task
from character.models import Character, CharacterEquipment


@shared_task
def create_character_task(user_id):
    User = get_user_model()
    user = User.objects.get(id=user_id)
    try:
        Character.objects.create(user=user)
    except Exception as exc:
        print(exc)

@shared_task
def create_character_equipment_task(character_id):
    try:
        character = Character.objects.get(id=character_id)
        CharacterEquipment.objects.create(character=character)
    except Exception as exc:
        print(exc)