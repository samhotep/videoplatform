from .serializers import VideoSerializer
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from videoapp.models import Video

class VideoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Viewset for loading videos filtered by type
    """
    #queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        video_type = self.kwargs['video_type']
        return Video.objects.filter(video_type=video_type)

    def list(self, request, video_type):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

