from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view
from .utils import get_md5_hash
from django.db.models import Q
from PIL import Image as ImageFiles
import imagehash


@api_view(['POST'])
def upload(request, format=None):
    return uploadLoose(request, format)


def uploadLoose(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        # check for the hash already exists here.
        phash_str = str(imagehash.phash(ImageFiles.open(uploaded_image)))
        phash = int(phash_str, 16)
        print(phash)
        # Define the cutoff value
        cutoff = 10  # Adjust as needed
        lower_bound = str(phash - cutoff)
        upper_bound = str(phash + cutoff)

        print(lower_bound, upper_bound)
        # Create a query to filter records within the specified range

        records_in_range = models.Image.objects.filter(
            Q(hash_id__gte=lower_bound) &
            Q(hash_id__lte=upper_bound)
        )

        print(records_in_range)

        if records_in_range.exists():
            return JsonResponse({'message': 'Image already exists'})

        image = models.Image(image=uploaded_image,
                             hash_id=phash)
        image.save()

        return JsonResponse({'message': 'Image uploaded successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)

# exact match


def uploadTight(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        # check for the hash already exists here.
        hash_id = get_md5_hash(uploaded_image)
        try:
            image = models.Image.objects.get(hash_id=hash_id)
            print('Image already exists')
            return JsonResponse({'message': 'Image already exists'})
        except models.Image.DoesNotExist:
            image = models.Image(image=uploaded_image,
                                 hash_id=hash_id)
            image.save()
            print('created a new entry')

        return JsonResponse({'message': 'Image uploaded successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)
