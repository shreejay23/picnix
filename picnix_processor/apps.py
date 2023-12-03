from django.apps import AppConfig
from picnix_backbone.signals import task_signal
from .tasks import process_task


class PicnixProcessorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "picnix_processor"

    def ready(self):
        task_signal.connect(process_task, weak=False)
