from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view
from picnix_backbone.app_utils import *
from picnix_backbone.signals import task_signal
from picnix_processor.tasks import process_task


@api_view(['POST'])
def upload(request, format=None):
    if not request.FILES.get('image'):
        return JsonResponse({'error': 'No image file provided'}, status=400)

    uploaded_image = request.FILES['image']
    image = models.Image(image=uploaded_image)
    image.save()

    # task_signal.send(sender="SendingApp", data="Some data to process")
    process_task.delay(sender="SendingApp", data="Some data to process")
    return JsonResponse({'message': 'Image uploaded successfully'})


@api_view(['POST'])
def delete_all_images(request, format=None):
    models.Image.objects.all().delete()
    return JsonResponse({'message': 'Images deleted successfully'})
