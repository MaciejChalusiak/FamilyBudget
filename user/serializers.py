from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "password"]


class ShowSharedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username"]
