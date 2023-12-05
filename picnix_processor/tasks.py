import traceback
import numpy as np
from celery import shared_task
from django.shortcuts import get_object_or_404

from picnix_backbone import models
from picnix_processor.app_utils import *
from picnix_processor.ImageFeatures import ImageFeatures


def identify_cluster(cluster_centers, image_moments):
    distances = np.linalg.norm(
        np.array(cluster_centers) - np.array(image_moments), axis=1)
    sorted_clusters = np.argsort(distances)

    return distances, sorted_clusters[:2]


def check_for_exact_image_match(cluster_label, image1_path):
    imageClusters = models.ImageCluster.objects.filter(
        cluster_id=cluster_label)
    for imageCluster in imageClusters:
        image2 = get_object_or_404(models.Image, id=imageCluster.image_id)
        image2_path = get_image_path(image2)
        if is_exactly_same(image1_path, image2_path):
            return image2, True
    return None, False


def process_uploaded_image(post_id, image_id):
    image = get_object_or_404(models.Image, id=image_id)
    img_path = get_image_path(image)

    threshold = 0.00006

    clusterInfo_objects = models.ClusterInfo.objects.all().order_by('cluster_id')
    cluster_centers = [get_cluster_center_in_nums(
        clusterInfo_object.cluster_center) for clusterInfo_object in clusterInfo_objects]
    cluster_labels = [
        clusterInfo_object.cluster_id for clusterInfo_object in clusterInfo_objects]
    # print("LABELS")
    # print(cluster_labels)

    processed_image = ImageFeatures().preprocess_image(img_path)
    image_moments = ImageFeatures().calculate_moment_invariants(processed_image)
    n = len(cluster_labels)

    if n < 1:
        image_cluster_label = n + 1
        new_clusterInfo = models.ClusterInfo(
            cluster_id=image_cluster_label, cluster_center=get_cluster_center_in_text(image_moments))
        new_clusterInfo.save()

        imageCluster = models.ImageCluster(
            cluster_id=image_cluster_label, image_id=image.id)
        imageCluster.save()

        return image_cluster_label

    scores, sorted_clusters_indices = identify_cluster(
        cluster_centers, image_moments)

    # print("Scores:")
    # print(scores)

    ind = sorted_clusters_indices[0]
    exact_match_flag = False
    exact_match_image = None
    exact_match_image, exact_match_temp_flag = check_for_exact_image_match(
        cluster_labels[sorted_clusters_indices[-1]], img_path)
    if scores[sorted_clusters_indices[-1]] <= threshold and exact_match_temp_flag:
        ind = sorted_clusters_indices[-1]
        exact_match_flag = True
    exact_match_image, exact_match_temp_flag = check_for_exact_image_match(
        cluster_labels[sorted_clusters_indices[0]], img_path)
    if (exact_match_flag == False) and exact_match_temp_flag:
        exact_match_flag = True

    n = len(cluster_labels)
    flag = False
    # print("IND " + str(ind))
    image_cluster_label = cluster_labels[ind]

    if scores[ind] > threshold:
        flag = True
    elif not exact_match_flag:
        near_duplicate_cluster = models.ClusterInfo.objects.get(
            cluster_id=image_cluster_label)
        near_duplicate_cluster_centers = get_cluster_center_in_nums(
            near_duplicate_cluster.cluster_center)
        # print("Cluster centers")
        prev_cluster_length = models.ImageCluster.objects.filter(
            cluster_id=image_cluster_label).count()
        temp_numerator = [prev_cluster_length *
                          num for num in near_duplicate_cluster_centers]
        for i in range(len(image_moments)):
            temp_numerator[i] += image_moments[i]
        new_cluster_centers = [num / (prev_cluster_length + 1)
                               for num in temp_numerator]
        models.ClusterInfo.objects.filter(cluster_id=image_cluster_label).update(
            cluster_center=get_cluster_center_in_text(new_cluster_centers))

    if flag:
        image_cluster_label = n + 1
        new_clusterInfo = models.ClusterInfo(
            cluster_id=image_cluster_label, cluster_center=get_cluster_center_in_text(image_moments))
        new_clusterInfo.save()

    print(str(image_cluster_label) + " is the cluster ID of the new image")

    to_assign_image_id = image.id
    if exact_match_flag:
        to_assign_image_id = exact_match_image.id
        print("The exact match flag is True")
        models.Post.objects.filter(id=post_id).update(image=exact_match_image)
        image.delete()
        models.Image.objects.filter(id=exact_match_image.id).update(
            num_refs=exact_match_image.num_refs + 1)
        # TODO Delete Handling

    imageCluster = models.ImageCluster(
        cluster_id=image_cluster_label, image_id=to_assign_image_id)
    imageCluster.save()

    return image_cluster_label


@shared_task
def process_task(post_id, image_id, **kwargs):
    # Your processing logic here
    print("Received Post: {} image: {}".format(post_id, image_id))
    try:
        print("Cluster Label: " + str(process_uploaded_image(post_id, image_id)))
        print("Processed image: {}".format(image_id))
    except Exception as e:
        print(traceback.format_exc())
        print("Error processing image: {}".format(e))
