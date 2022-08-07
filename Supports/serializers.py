from rest_framework import serializers
from .models import Requests, Tikets


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = "__all__"


class RequestsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ("users", "topic", "status")


class TiketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tikets
        fields = "__all__"


class TiketsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tikets
        fields = ("request", "user", "message")
