from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from ca.core.models import Event


class TestEventView(APITransactionTestCase):
    def setUp(self) -> None:
        # given
        self.url = reverse("event-list")

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
            self.url,
            self.body,
            format="json"
        )

    def test_post_to_create_event(self):
        # then
        self.assertEqual(self.resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)

    def test_put_to_update_event(self):
        # given
        new_body = self.body.copy()
        new_name = 'different pageview'
        new_body['name'] = new_name

        # when
        put_url = reverse('event-detail', kwargs={'pk': str(Event.objects.last().pk)})
        put_resp = self.client.put(
            put_url,
            new_body,
            format="json",
        )

        # then
        updated_event = self.client.get(put_url)
        # self.assertEqual(put_resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(new_name, updated_event.data['name'])