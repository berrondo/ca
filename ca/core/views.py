from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_for_update().all().order_by("-timestamp")
    serializer_class = EventSerializer
