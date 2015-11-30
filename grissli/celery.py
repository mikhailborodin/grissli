from __future__ import absolute_import
from django.conf import settings

from celery import Celery
import os
import djcelery
djcelery.setup_loader()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grissli.settings')


app = Celery('grissli')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
