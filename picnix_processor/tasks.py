# Create your views here.
# processor/tasks.py

from celery import shared_task
from picnix_backbone.signals import task_signal


@shared_task
def process_task(data, **kwargs):
    # Your processing logic here
    print(f"Processing task with data: {data}")
    import time
    time.sleep(5)
    print("Task completed")
