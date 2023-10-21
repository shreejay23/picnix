import hashlib


def get_md5_hash(image):
    md5_hash = hashlib.md5()
    for chunk in image.chunks():
        md5_hash.update(chunk)

    return md5_hash.hexdigest()
