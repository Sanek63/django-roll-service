from celery import shared_task


@shared_task
def example():
    return 'hello'
