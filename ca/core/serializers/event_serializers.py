from django.utils import timezone

from ca.core.models import Event, RawEvent
from rest_framework import serializers


class RawEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawEvent
        fields = ["payload", "status", "created_at"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["session_id", "category", "name", "data", "timestamp"]
