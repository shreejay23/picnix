import os


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