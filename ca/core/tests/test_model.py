from uuid import UUID
from django.test import TestCase
from ..models import Event


class EventTestCase(TestCase):
    def test_create_an_event(self):
        # given
        self.event = Event(
            session_id="e2085be5-9137-4e4e-80b5-f1ffddc25423",
            category="page interaction",
            name="pageview",
            data={
                "host": "www.example.com",
                "path": "/"
            },
            timestamp="2021-01-01 09:15:27.243860",
        )
        previous_count = Event.objects.count()

        # when
        self.event.save()

        # then
        new_count = Event.objects.count()
        self.assertEqual(previous_count + 1, new_count)
        self.assertEqual(
            UUID("e2085be5-9137-4e4e-80b5-f1ffddc25423"),
            Event.objects.last().session_id
        )
