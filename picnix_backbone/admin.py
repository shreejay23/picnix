from django.contrib import admin
from .models import Image, Post, ImageCluster, ClusterInfo

admin.site.register(Image)
admin.site.register(Post)
admin.site.register(ImageCluster)
admin.site.register(ClusterInfo)
