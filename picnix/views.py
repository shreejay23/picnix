from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view
from .utils import get_md5_hash


@api_view(['POST'])
def upload(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        # check for the hash already exists here.
        new_image = models.Image(image=uploaded_image,
                                 hash_id=get_md5_hash(uploaded_image))
        new_image.save()
        return JsonResponse({'message': 'Image uploaded successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)
