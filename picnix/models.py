from django.db import models


class Image(models.Model):
    hash_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self) -> str:
        return self.hash_id


class Post(models.Model):
    id = models.TextField(max_length=200, primary_key=True)
    file_id = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.file_id
