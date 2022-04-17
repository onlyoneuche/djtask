import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djtask.settings')

app = Celery('djtask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
