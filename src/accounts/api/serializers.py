from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "name", "image")
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}
        read_only_Fields = ("id",)