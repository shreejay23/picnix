import os
import numpy as np
from celery import shared_task
from sklearn.cluster import KMeans
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from picnix_backbone import models
from picnix_processor.app_utils import *
from picnix_processor.ImageFeatures import ImageFeatures


def identify_cluster(cluster_centers, test_moments):
    distances = np.linalg.norm(np.array(cluster_centers) - np.array(test_moments), axis=1)
    sorted_clusters = np.argsort(distances)

    return distances, sorted_clusters

def process_uploaded_image(image_id):
    image = get_object_or_404(models.Image, id=image_id)
    img_path = get_image_path(image)

    threshold = 0.0003

    clusterInfo_objects = models.ClusterInfo.objects.all().order_by('cluster_id')
    cluster_centers = [get_cluster_center_in_nums(clusterInfo_object.cluster_center) for clusterInfo_object in clusterInfo_objects]
    cluster_labels = [clusterInfo_object.cluster_id for clusterInfo_object in clusterInfo_objects]
    # print("LABELS")
    # print(cluster_labels)

    test_image_processed = ImageFeatures().preprocess_image(img_path)
    test_moments = ImageFeatures().calculate_moment_invariants(test_image_processed)
    n = len(cluster_labels)

    if n < 1:
        test_image_cluster_label = n + 1
        new_clusterInfo = models.ClusterInfo(cluster_id = test_image_cluster_label, cluster_center = get_cluster_center_in_text(test_moments))
        new_clusterInfo.save()

        test_imageCluster = models.ImageCluster(cluster_id = test_image_cluster_label, image_id = image.id)
        test_imageCluster.save()

        return JsonResponse({'message': 'Image processed successfully'})

    scores, sorted_clusters_indices = identify_cluster(cluster_centers, test_moments)

    # print("Scores:")
    # print(scores)

    i = 0
    test_image_cluster_label = 0
    n = len(cluster_labels)
    flag = False
    while i < n:
        ind = sorted_clusters_indices[i]
        # print("IND " + str(ind))
        cluster_score = scores[ind]
        test_image_cluster_label = cluster_labels[ind]
        if cluster_score > threshold:
            flag = True
            break
        else:
            near_duplicate_cluster = models.ClusterInfo.objects.get(cluster_id = test_image_cluster_label)
            near_duplicate_cluster_centers = get_cluster_center_in_nums(near_duplicate_cluster.cluster_center)
            # print("Cluster centers")
            prev_cluster_length = models.ImageCluster.objects.filter(cluster_id = test_image_cluster_label).count()
            # return JsonResponse({'message': 'NOOOOOOOOOOOOOOOOOOOO'})
            temp_numerator = [prev_cluster_length * num for num in near_duplicate_cluster_centers]
            for i in range(len(test_moments)):
                temp_numerator[i] += test_moments[i]
            new_cluster_centers = [num / (prev_cluster_length + 1) for num in temp_numerator]
            models.ClusterInfo.objects.filter(cluster_id = test_image_cluster_label).update(cluster_center = get_cluster_center_in_text(new_cluster_centers))
            break
        i += 1

    if i == n or flag:
        test_image_cluster_label = n + 1
        new_clusterInfo = models.ClusterInfo(cluster_id = test_image_cluster_label, cluster_center = get_cluster_center_in_text(test_moments))
        new_clusterInfo.save()

    print(str(test_image_cluster_label) + " is the cluster ID of the new image")
    test_imageCluster = models.ImageCluster(cluster_id = test_image_cluster_label, image_id = image.id)
    test_imageCluster.save()

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
