import numpy as np
from sklearn.cluster import KMeans
from django.http import JsonResponse

from rest_framework.decorators import api_view
from . import models
from picnix_backbone.app_utils import *
from picnix_backbone.ImageFeatures import ImageFeatures


def identify_cluster(post_image, cluster_centers):
    post_moments = ImageFeatures().calculate_moment_invariants(post_image)

    distances = np.linalg.norm(
        np.array(cluster_centers) - np.array(post_moments), axis=1)

    top_clusters = np.argsort(distances)[:2]

    return top_clusters


def recluster_images(num_clusters):
    db_images = models.Image.objects.all()
    features, labels = ImageFeatures().extract_features_from_db_images(db_images)

    def cluster_images(features, num_clusters):
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(features)
        return kmeans.labels_, kmeans.cluster_centers_

    cluster_labels, cluster_centers = cluster_images(
        features, num_clusters)

    return labels, cluster_labels, cluster_centers


@api_view(['POST'])
def process_uploaded_image(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']

        # saving image before processing. will be removed
        image = models.Image(image=uploaded_image)
        image.save()
        uploaded_image = models.Image.objects.last()
        img_path = get_image_path(uploaded_image)

        # future work: only run this if total images > threshold
        num_clusters = 5
        labels, cluster_labels, cluster_centers = recluster_images(
            num_clusters)
        print_clusters(num_clusters, labels, cluster_labels)

        top_clusters = identify_cluster(img_path, cluster_centers)

        print(f"\nTest image belongs to clusters: {top_clusters}")

        return JsonResponse({'message': 'Image processed successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)
