from django.db import models

# Create your models here.

class VideoType(models.Model):
    """
    Model for classification of video types
    """
    
    name = models.CharField(max_length=128, blank=False)

class Video(models.Model):
    """
    Model for upload videos
    """

    title = models.CharField(max_length=128, blank=False)
    speaker = models.CharField(max_length=128, blank=False)
    date = models.DateTimeField()
    video_type = models.ForeignKey("VideoType", on_delete=models.CASCADE, blank=False)
    url = models.URLField(blank=False)
