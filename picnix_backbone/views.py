from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from . import models
from rest_framework.decorators import api_view
from picnix_processor.tasks import process_task


@api_view(['POST'])
def upload(request, format=None):
    if not request.FILES.get('image'):
        return JsonResponse({'error': 'No image file provided'}, status=400)

    uploaded_image = request.FILES['image']

    data = request.data
    username = data.get('username', '')
    description = data.get('description', '')

    if not username or not description:
        return JsonResponse({'error': 'All required fields not present'}, status=400)

    image = models.Image(image=uploaded_image)
    image.save()

    post = models.Post(image=image, user=username, description=description)
    post.save()

    process_task.delay(sender="Uploader", image_id=image.id)
    return JsonResponse({'message': 'Image uploaded successfully', 'body': {'postId': post.id}})


@api_view(['GET'])
def get_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    response_data = {
        'id': post.id,
        'imageId': post.image.id
    }

    return JsonResponse(response_data)


@api_view(['POST'])
def delete_all_images(request, format=None):
    models.Image.objects.all().delete()
    return JsonResponse({'message': 'Images deleted successfully'})
