from rest_framework import viewsets, mixins

from ca.core.models import Event
from ca.core.serializers import EventSerializer

from .models import Event
from .serializers import EventSerializer



class EventViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
