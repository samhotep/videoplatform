from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from videoapp.models import Video

alphanumeric = RegexValidator(r"^[0-9a-zA-Z]*$", "Only alphanumeric characters allowed (0-9, A-Z, a-z)")

class VideoSerializer(serializers.ModelSerializer):

    file = serializers.FileField(source='video_data')

    class Meta:
        model = Video
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(validators=[alphanumeric])

    class Meta:
        model = User
        fields = ["username", "password"]
