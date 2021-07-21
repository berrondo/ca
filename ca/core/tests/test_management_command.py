from django.core.management import call_command
from django.test import TestCase

from ca.core.models import RawEvent, Event
from ca.core.tests import fixtures


class ProcessEventsTest(TestCase):
    def test_command_output(self):
        # given
        RawEvent.objects.bulk_create([
            RawEvent(payload=fixtures.re1, status=RawEvent.Status.RECEIVED),
            RawEvent(payload=fixtures.re2, status=RawEvent.Status.RECEIVED),
            RawEvent(payload=fixtures.re3, status=RawEvent.Status.PROCESSED),
        ])

        self.assertEqual(2, RawEvent.objects.filter(status=RawEvent.Status.RECEIVED).count())
        self.assertEqual(0, Event.objects.all().count())

        # when
        call_command('process_events')

        # then
        self.assertEqual(3, RawEvent.objects.filter(status=RawEvent.Status.PROCESSED).count())
        self.assertEqual(2, Event.objects.all().count())

