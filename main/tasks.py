from __future__ import absolute_import
from main.models import Url, Result
from celery import shared_task
from bs4 import BeautifulSoup
from datetime import datetime
import urllib


@shared_task
def parsing_url(instance=None):
    if instance:
        html_doc = urllib.urlopen(instance.url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        obj = Result(url=instance, title=soup.title, encoding=soup.original_encoding)
        obj.save()
        instance.datetime = datetime.now()
        instance.save()
    else:
        print 'no url'
