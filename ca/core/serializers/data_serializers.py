from rest_framework import serializers

from ca.core.serializers.event_serializers import EventSerializer


class EventAndDataSerializer(EventSerializer):
    @property
    def event_type(self):
        if event := self.initial_data:
            if category := event.get('category'):
                if name := event.get('name'):
                    return " ".join((category, name))
        return ""

    @property
    def event_type_data(self):
        if event := self.initial_data:
            if data := event.get('data'):
                return data
        return ""

    @property
    def event_type_data_serializer(self):
        return _event_type_serializer.get(self.event_type, MissingCategorySerializer)

    def event_type_data_is_valid(self):
        self.instance_event_type_data_serializer = self.event_type_data_serializer(data=self.event_type_data)
        return self.instance_event_type_data_serializer.is_valid()


class PageViewSerializer(serializers.Serializer):
    host = serializers.CharField()
    path = serializers.CharField()


class PageClickSerializer(PageViewSerializer):
    element = serializers.CharField()


class FormSubmitSerializer(PageViewSerializer):
    form = serializers.JSONField()


class MissingCategorySerializer():
    errors = []

    def __init__(self, data):
        ...

    def is_valid(self):
        return False


_event_type_serializer = {
    "page interaction pageview": PageViewSerializer,
    "page interaction cta click": PageClickSerializer,
    "form interaction submit": FormSubmitSerializer,
}
