from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from ca.core.models import Event, RawEvent
from ca.core.serializers.event_serializers import EventSerializer, RawEventSerializer


class RawEventViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):
    """it's a viewsets.ReadOnlyModelViewSet"""

    queryset = RawEvent.objects.all()
    serializer_class = RawEventSerializer


class EventViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # here is the hack!
    def create(self, request, *args, **kwargs):
        """is now used to create a RawEvent instead of an Event!"""
        serializer = RawEventSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
