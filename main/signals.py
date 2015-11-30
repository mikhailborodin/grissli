from main.tasks import parsing_url


def add_task(sender, instance, created, **kwargs):
    if created:
        parsing_url.delay(instance=instance)