from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view
from picnix_backbone.app_utils import *


@api_view(['POST'])
def upload(request, format=None):
    return uploadLoose(request, format)


def uploadLoose(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image = models.Image(image=uploaded_image)
        image.save()

        return JsonResponse({'message': 'Image uploaded successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)


@api_view(['POST'])
def delete_all_images(request, format=None):
    models.Image.objects.all().delete()
    return JsonResponse({'message': 'Images deleted successfully'})
