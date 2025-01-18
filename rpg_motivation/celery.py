import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rpg_motivation.settings")
app = Celery("rpg_motivation")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()