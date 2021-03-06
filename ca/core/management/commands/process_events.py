from django.core.management.base import BaseCommand
from ca.core.models import RawEvent
from ca.core.serializers.data_serializers import EventAndDataSerializer


class Command(BaseCommand):
    help = 'Process received Events'

    def handle(self, *args, **options):
        raw_events = RawEvent.objects.filter(status=RawEvent.Status.RECEIVED)

        for raw_event in raw_events:
            serializer = EventAndDataSerializer(data=raw_event.payload)

            if serializer.is_valid():
                if serializer.event_type_data_is_valid():
                    serializer.save()
                    raw_event.status = RawEvent.Status.PROCESSED
                    raw_event.save()
                    self.stdout.write(self.style.SUCCESS('Successfully processed Event "%s"' % raw_event.pk))
                    continue

                else:
                    serializer = serializer.instance_event_type_data_serializer

            self.stdout.write(self.style.ERROR(str(raw_event.payload)))
            self.stdout.write(self.style.ERROR(str(serializer.errors)))
            raw_event.status = RawEvent.Status.INVALID
            raw_event.errors = serializer.errors
            raw_event.save()
