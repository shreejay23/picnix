from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self) -> str:
        return str(self.id)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    user = models.TextField(max_length=20)
    description = models.TextField(max_length=100, default='')

    def __str__(self) -> str:
        return str(self.id)

class ImageCluster(models.Model):
    cluster_id = models.IntegerField()
    image_id = models.IntegerField()

class ClusterInfo(models.Model):
    id = models.AutoField(primary_key=True)
    cluster_id = models.IntegerField()
    cluster_center = models.TextField()