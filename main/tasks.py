from __future__ import absolute_import
from celery import shared_task


@shared_task
def parsing_url(url=None):
    print url
