import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from ..models import Event


class TestEventView(APITransactionTestCase):
    def test_post_event(self):
        # given
        url = reverse("event-list")
        body = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.ca.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        # when
        response = self.client.post(
            url,
            body,
            format="json"
        )

        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(
            Event.objects.get().session_id,
            uuid.UUID("e2085be5-9137-4e4e-80b5-f1ffddc25423"),
        )
