from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

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

    image = models.Image(image=uploaded_image, num_refs=0)
    image.save()

    post = models.Post(image=image, user=username, description=description)
    post.save()

    process_task.delay(sender="Uploader", post_id=post.id,
                       image_id=image.id)  # send post id
    return JsonResponse({'message': 'Image uploaded successfully', 'body': {'postId': post.id}})


@api_view(['GET'])
def get_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    response_data = {
        'id': post.id,
        'imageId': post.image.id
    }

    return JsonResponse(response_data)


@api_view(['GET'])
def get_all_posts(request, format=None):
    PAGE_SIZE = 10

    page = int(request.GET.get('page', '1'))
    similar_to = request.GET.get('similar_to')
    duplicate_to = request.GET.get('duplicate_to')

    _from = (page-1)*PAGE_SIZE
    _to = (page)*PAGE_SIZE

    if similar_to and duplicate_to:
        return JsonResponse({'error': 'Bad Request'}, status=400)

    posts = []
    if similar_to:
        similar_post = get_object_or_404(models.Post, id=similar_to)
        cluster_id = get_object_or_404(
            models.ImageCluster, image_id=similar_post.image.id).cluster_id
        image_ids_in_cluster = models.ImageCluster.objects.filter(
            cluster_id=cluster_id).values_list('image_id', flat=True)
        posts = models.Post.objects.filter(
            image__id__in=image_ids_in_cluster).order_by('-timestamp')[_from:_to]
    elif duplicate_to:
        duplicate_post = get_object_or_404(models.Post, id=duplicate_to)
        posts = get_list_or_404(
            models.Post.objects.filter(
                image__id=duplicate_post.image.id).order_by('-timestamp')[_from:_to]
        )
    else:
        posts = models.Post.objects.all().order_by('-timestamp')[_from:_to]

    image_ids = list(map(lambda post: post.image.id, posts))
    image_similarity_map = get_image_similarities(image_ids)

    response_data = [{
        'id': post.id,
        'image': request.build_absolute_uri(post.image.image.url),
        'desc': post.description,
        'user': post.user,
        'similars': image_similarity_map[post.image.id],
        'duplicates': post.image.num_refs,
    } for post in posts]

    return JsonResponse(response_data, safe=False)


def get_image_similarities(image_ids):
    image_cluster_map = {image.image_id: image.cluster_id for image in models.ImageCluster.objects.filter(
        image_id__in=image_ids)}
    print(image_cluster_map)
    cluster_counts = models.ImageCluster.objects.values(
        'cluster_id').annotate(count=Count('cluster_id'))
    cluster_count_map = {}
    for cluster_count in cluster_counts:
        cluster_id = cluster_count['cluster_id']
        cluster_count_map[cluster_id] = cluster_count['count']

    image_similarity_map = {}
    for image_id in image_ids:
        cluster_id = image_cluster_map[image_id]
        image_similarity_map[image_id] = cluster_count_map[cluster_id]

    return image_similarity_map


@api_view(['POST'])
def delete_all_images(request, format=None):
    models.Image.objects.all().delete()
    return JsonResponse({'message': 'Images deleted successfully'})
