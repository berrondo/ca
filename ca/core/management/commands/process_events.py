from django.core.management.base import BaseCommand
from ca.core.models import RawEvent
from ca.core.serializers.event_serializers import EventSerializer


class Command(BaseCommand):
    help = 'Process received Events'

    def handle(self, *args, **options):
        raw_events = RawEvent.objects.filter(status=RawEvent.Status.RECEIVED)

        for raw_event in raw_events:
            data = raw_event.payload
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                raw_event.status = RawEvent.Status.PROCESSED
                raw_event.save()
                self.stdout.write(self.style.SUCCESS('Successfully processed Event "%s"' % raw_event.pk))
            else:
                self.stdout.write(self.style.ERROR(raw_event.payload))
                self.stdout.write(self.style.ERROR(serializer.errors))
                raw_event.status = RawEvent.Status.INVALID
                raw_event.save()
