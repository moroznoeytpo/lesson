import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson.settings')

app = Celery('lesson')

app.config_from_object('lesson.settings', namespace='CELERY')

app.autodiscover_tasks()
