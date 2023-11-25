from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self) -> str:
        return self.id


class Post(models.Model):
    id = models.TextField(max_length=200, primary_key=True)
    image_id = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    user = models.TextField(max_length=20)
    description = models.TextField(max_length=100, default='')

    def __str__(self) -> str:
        return self.id
