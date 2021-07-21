from django.test import TestCase

from ca.core.serializers.event_serializers import EventSerializer
from ca.core.tests import fixtures


class TestEventSerializer(TestCase):
    def test_timestamp_cannot_be_in_the_future(self):
        # given
        future_re1 = fixtures.re1.copy()
        future_re1['timestamp'] = '5000-01-01 09:15:27.243860'
        serializer = EventSerializer(data=future_re1)

        # when
        serializer.is_valid()

        # then
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'timestamp'})


class TestRawEventSerializer(TestCase):
    ...


class TestEventAndDataserializer(TestCase):
    ...


class TestPageViewSerializer(TestCase):
    ...


class TestPageClickSerializer(TestCase):
    ...


class TestFormSubmitSerializer(TestCase):
    ...
