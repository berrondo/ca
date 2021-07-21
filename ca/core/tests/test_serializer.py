from django.test import TestCase

from ca.core.serializers.data_serializers import (
    PageViewSerializer,
    PageClickSerializer,
    FormSubmitSerializer,
)
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


class TestDataSerializer(TestCase):
    def test_path_is_a_required_data_field(self):
        # given
        required_field = 'path'
        data_missing_a_field = fixtures.page_interaction_pageview["data"].copy()
        del data_missing_a_field[required_field]
        serializer = PageViewSerializer(data=data_missing_a_field)

        # when
        serializer.is_valid()

        # then
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {required_field})

    def test_element_is_a_required_data_field(self):
        # given
        required_field = 'element'
        data_missing_a_field = fixtures.page_interaction_cta_click["data"].copy()
        del data_missing_a_field[required_field]
        serializer = PageClickSerializer(data=data_missing_a_field)

        # when
        serializer.is_valid()

        # then
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {required_field})

    def test_form_is_a_required_data_field(self):
        # given
        required_field = 'form'
        data_missing_a_field = fixtures.form_interaction_submit["data"].copy()
        del data_missing_a_field[required_field]
        serializer = FormSubmitSerializer(data=data_missing_a_field)

        # when
        serializer.is_valid()

        # then
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {required_field})