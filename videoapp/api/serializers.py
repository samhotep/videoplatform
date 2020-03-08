from rest_framework import serializers
from videoapp.models import Video

class VideoSerializer(serializers.ModelSerializer):

    file = serializers.FileField(source='video_data')

    class Meta:
        model = Video
        fields = ['__all__']
