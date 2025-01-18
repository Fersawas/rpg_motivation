from django.apps import AppConfig


class CharacterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "character"

    def ready(self) -> None:
        import character.signals