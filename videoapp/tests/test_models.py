from django.test import TestCase
from videoapp.models import VideoType, Video

# Create your tests here.

class ModelsTestCase(TestCase):

    def setUp(self):
        self.videoType = VideoType.objects.create(name="Morning Education")
        self.video = Video.objects.create(
                title="Test Video",
                speaker="Test Speaker",
                date="2020-02-02",
                video_type=self.videoType,
                url="test_video_1/"
            )

    def test_videotype_created(self):
        self.assertTrue(isinstance(self.videoType, VideoType))

    def test_videotype_matches(self):
        self.assertEqual(self.videoType.name, "Morning Education")
    