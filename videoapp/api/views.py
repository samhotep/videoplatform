from .serializers import VideoSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from videoapp.models import Video

class VideoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Viewset for loading videos filtered by type
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def list(self, request, video_type):
        self.queryset = Video.objects.filter(video_type=video_type)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    Viewset for handling user logins
    """

    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data["username"], password=serializer.data["password"])
            print("Checking user")
            if user is not None:
                return Response(
                    {
                        "status": "SUCCESS"
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "status": "FAILED",
                        "message": "Unable to authenticate user"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    "status": "FAILED",
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )
