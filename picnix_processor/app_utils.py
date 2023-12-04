import os
import cv2

def get_image_path(uploaded_image):
    directory = uploaded_image.image.url[1:].split('/')
    img_path = os.path.join(*directory)
    return img_path


def print_clusters(num_clusters, labels, cluster_labels):
    for cluster in range(num_clusters):
        print(f"\nCluster {cluster}:")
        for i, label in enumerate(labels):
            if cluster_labels[i] == cluster:
                print(label)

def get_cluster_center_in_text(num_data):
    cluster_center = ','.join(map(str, num_data))
    return cluster_center

def get_cluster_center_in_nums(cluster_center_text):
    text = cluster_center_text.split(',')
    nums = list(float(x) for x in text)
    return nums

def is_exactly_same(image1_path, image2_path) -> bool:
    """
    Params:
        image1_path and image2_path
    
    Returns:
        bool: True if the images are exactly the same, False otherwise
    
    Obtains the pixel-wise difference between the two images and checks if the difference(in all three color channel) is 0 or not and returns accordingly.
    """
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    if image1.shape == image2.shape:
        difference = cv2.subtract(image1, image2) # This operation calculates the pixel-wise difference between the two images.
        blue, green, red = cv2.split(difference) # Split the difference in three color channels: blue, green, and red.

        # Check if all three color channels in the difference image have no nonzero (non-black) pixels.
        if cv2.countNonZero(red) == 0 and cv2.countNonZero(green) == 0 and cv2.countNonZero(blue) == 0:
            return True

    return False