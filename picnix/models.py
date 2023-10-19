from django.db import models


class ImageFile(models.Model):
    hash_id = models.TextField(max_length=200, primary_key=True)
    location = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.location


class Post(models.Model):
    id = models.TextField(max_length=200, primary_key=True)
    file_id = models.ForeignKey(ImageFile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.file_id
