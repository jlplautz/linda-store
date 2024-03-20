import os

from celery import Celery

# from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lindaStore.settings')

app = Celery('lindaStore')

# namespace='CELERY' -> significar que toda configuração relacionada
# deverá ter o prefix 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
