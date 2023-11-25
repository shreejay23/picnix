from django.http import JsonResponse
from . import models
from rest_framework.decorators import api_view
from .utils import get_md5_hash
from django.db.models import Q
from PIL import Image as ImageFiles
import imagehash
import cv2
import os
import numpy as np
from sklearn.cluster import KMeans
from django.core.files.uploadedfile import InMemoryUploadedFile


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

# exact match


# def uploadTight(request, format=None):
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_image = request.FILES['image']
#         # check for the hash already exists here.
#         hash_id = get_md5_hash(uploaded_image)
#         try:
#             image = models.Image.objects.get(hash_id=hash_id)
#             print('Image already exists')
#             return JsonResponse({'message': 'Image already exists'})
#         except models.Image.DoesNotExist:
#             image = models.Image(image=uploaded_image,
#                                  hash_id=hash_id)
#             image.save()
#             print('created a new entry')

#         return JsonResponse({'message': 'Image uploaded successfully'})

#     return JsonResponse({'error': 'No image file provided'}, status=400)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    resized = cv2.resize(gray, (256, 256), interpolation=cv2.INTER_CUBIC)

    equalized = cv2.equalizeHist(resized)
    
    return equalized

def calculate_moment_invariants(image):
    moments = cv2.moments(image)
    
    eta20 = moments['mu20'] / moments['m00']**2
    eta02 = moments['mu02'] / moments['m00']**2
    eta11 = moments['mu11'] / moments['m00']**2
    eta30 = moments['mu30'] / moments['m00']**2
    eta12 = moments['mu12'] / moments['m00']**2
    eta21 = moments['mu21'] / moments['m00']**2
    eta03 = moments['mu03'] / moments['m00']**2
    
    phi1 = eta20 + eta02
    phi2 = (eta20 - eta02)**2 + 4 * eta11**2
    phi3 = (eta30 - 3 * eta12)**2 + (3 * eta21 - eta03)**2
    
    return phi1, phi2, phi3

def extract_features_from_db_images(db_images):
    features = []
    labels = []
    
    for db_image in db_images:
            directories = db_image.image.url[1:].split('/')
            print(directories)
            img_path = os.path.join(*directories)
            preprocessed_image = preprocess_image(img_path)
            moments = calculate_moment_invariants(preprocessed_image)
            features.append(moments)
            labels.append(directories[-1])

    return features, labels

def cluster_images(features, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(features)
    return kmeans.labels_, kmeans.cluster_centers_

def test_image(post_image, cluster_centers):
    test_image = preprocess_image(post_image)
    
    test_moments = calculate_moment_invariants(test_image)
    
    distances = np.linalg.norm(np.array(cluster_centers) - np.array(test_moments), axis=1)
    
    top_clusters = np.argsort(distances)[:2]

    return top_clusters

@api_view(['POST'])
def delete_all_images(request, format=None):
    models.Image.objects.all().delete()
    return JsonResponse({'message': 'Images deleted successfully'})

@api_view(['POST'])
def process_test_image(request, format=None):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']

        image = models.Image(image=uploaded_image)
        image.save()
        db_test_image = models.Image.objects.last()

        db_images = models.Image.objects.all()
        
        num_clusters = 5
        
        features, labels = extract_features_from_db_images(db_images)
        
        cluster_labels, cluster_centers = cluster_images(features, num_clusters)
        
        for cluster in range(num_clusters):
            print(f"\nCluster {cluster}:")
            for i, label in enumerate(labels):
                if cluster_labels[i] == cluster:
                    print(label)

        directories = db_test_image.image.url[1:].split('/')
        img_path = os.path.join(*directories)
        top_clusters = test_image(img_path, cluster_centers)
        
        print(f"\nTest image belongs to clusters: {top_clusters}")

        return JsonResponse({'message': 'Image processed successfully'})

    return JsonResponse({'error': 'No image file provided'}, status=400)