from django.db import models
from .tasks import parsing_url


class Url(models.Model):
    url = models.URLField()
    minute = models.PositiveIntegerField(default=0)
    second = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.url


def add_task(sender, instance, created, **kwargs):
    parsing_url.delay(url=instance.url)

models.signals.post_save.connect(add_task, sender=Url)
