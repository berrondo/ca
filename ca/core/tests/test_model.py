from uuid import UUID
from django.test import TestCase

from . import fixtures
from ..models import Event


class TestEventModel(TestCase):
    def test_create_an_event(self):
        # given
        event = Event(**fixtures.page_interaction_pageview)
        previous_count = Event.objects.count()

        # when
        event.save()

        # then
        new_count = Event.objects.count()
        self.assertEqual(previous_count + 1, new_count)
        self.assertEqual(
            UUID("e2085be5-9137-4e4e-80b5-f1ffddc25423"),
            Event.objects.last().session_id
        )
