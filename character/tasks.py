from django.contrib.auth import get_user_model

from celery import shared_task
from celery.utils.log import get_task_logger

from character.models import Character, CharacterEquipment, Inventory


logger = get_task_logger(__name__)

@shared_task
def create_character_task(user_id):
    User = get_user_model()
    user = User.objects.get(id=user_id)
    try:
        res = Character.objects.create(user=user)
        logger.info(f'create character {res}')
    except Exception as exc:
        logger.error(exc)
        print(exc)

@shared_task
def create_character_equip_invent_task(character_id):
    try:
        character = Character.objects.get(id=character_id)
        equip =CharacterEquipment.objects.create(character=character)
        invent = Inventory.objects.create(character=character)
        logger.info(f'create character equipment {equip} and inventory {invent}')
    except Exception as exc:
        logger.error(exc)
        print(exc)