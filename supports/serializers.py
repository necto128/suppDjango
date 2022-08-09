from rest_framework import serializers
from .models import Request, Ticket


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("creator", "topic", "status")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("request", "user", "message")
