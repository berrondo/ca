from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from ca.core.models import Event, RawEvent


class TestRawEventView(APITransactionTestCase):
    def setUp(self) -> None:
        # given
        self.event_list_url = reverse("event-list")

        self.body = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.example.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        # when
        self.resp = self.client.post(
            self.event_list_url,
            self.body,
            format="json"
        )

        self.rawevent_detail_url = reverse('rawevent-detail', kwargs={'pk': str(RawEvent.objects.last().pk)})

        # then
        self.assertEqual(self.resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RawEvent.objects.count(), 1)

    def test_put_to_update_event_must_be_not_allowed(self):
        # given
        new_body = self.body.copy()
        new_name = 'different pageview'
        new_body['name'] = new_name

        # when
        resp = self.client.put(
            self.rawevent_detail_url,
            new_body,
            format="json",
        )

        # then
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_cannot_delete_event(self):
        # when
        resp = self.client.delete(
            self.rawevent_detail_url,
        )

        # then
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestEventView(APITransactionTestCase):
    def setUp(self) -> None:
        # given
        self.body = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.example.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        Event.objects.create(
            **self.body,
        )
        self.detail_url = reverse('event-detail', kwargs={'pk': str(Event.objects.last().pk)})

        # then
        self.assertEqual(Event.objects.count(), 1)

    def test_put_to_update_event_must_be_not_allowed(self):
        # given
        new_body = self.body.copy()
        new_name = 'different pageview'
        new_body['name'] = new_name

        # when
        resp = self.client.put(
            self.detail_url,
            new_body,
            format="json",
        )

        # then
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_cannot_delete_event(self):
        # when
        resp = self.client.delete(
            self.detail_url,
        )

        # then
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
