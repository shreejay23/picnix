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
