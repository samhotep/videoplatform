from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet, LoginViewSet

router = routers.SimpleRouter()
router.register(r"^video_list/(?P<video_type>.+)", VideoViewSet, basename="video_list")
router.register(r"login", LoginViewSet)
urlpatterns = router.urls