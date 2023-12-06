from django.db import models
import time


class ImageCluster(models.Model):
    image_id = models.IntegerField(primary_key=True)
    cluster_id = models.IntegerField()

    def __str__(self) -> str:
        return str(self.cluster_id) + "-" + str(self.image_id)

    class Meta:
        # Define a unique constraint to act as a composite primary key
        # unique_together = ('image_id', 'cluster_id')
        pass


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')
    num_refs = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    user = models.TextField(max_length=20)
    description = models.TextField(max_length=100, default='')
    timestamp = models.IntegerField(default=int(time.time()))

    def __str__(self) -> str:
        return str(self.id)


class ClusterInfo(models.Model):
    id = models.AutoField(primary_key=True)
    cluster_id = models.IntegerField()
    cluster_center = models.TextField()
