from django.db import models


class Url(models.Model):
    url = models.URLField(unique=True)
    minute = models.PositiveIntegerField(default=0)
    second = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url


class Result(models.Model):
    url = models.ForeignKey(Url)
    title = models.CharField(max_length=255)
    encoding = models.CharField(max_length=50)
    h1 = models.CharField(max_length=255, blank=True, null=True)


from main.signals import add_task
models.signals.post_save.connect(add_task, sender=Url)
