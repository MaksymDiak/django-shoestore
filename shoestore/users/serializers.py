from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
