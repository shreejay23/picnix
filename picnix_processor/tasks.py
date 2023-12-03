import numpy as np
from celery import shared_task
from sklearn.cluster import KMeans
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from picnix_backbone import models
from picnix_processor.app_utils import *
from picnix_processor.ImageFeatures import ImageFeatures


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


def process_uploaded_image(image_id):
    image = get_object_or_404(models.Image, id=image_id)
    img_path = get_image_path(image)

    # future work: only run this if total images > threshold
    num_clusters = 5
    labels, cluster_labels, cluster_centers = recluster_images(
        num_clusters)
    print_clusters(num_clusters, labels, cluster_labels)

    top_clusters = identify_cluster(img_path, cluster_centers)

    print(f"\nTest image belongs to clusters: {top_clusters}")

    return JsonResponse({'message': 'Image processed successfully'})


@shared_task
def process_task(image_id, **kwargs):
    # Your processing logic here
    print("Received image: {}".format(image_id))
    try:
        process_uploaded_image(image_id)
        print("Processed image: {}".format(image_id))
    except Exception as e:
        print("Error processing image: {}".format(e))
