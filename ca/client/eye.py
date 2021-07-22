import datetime
import uuid

import requests


class TheEye:
    url = 'http://localhost:8000/events/'

    @staticmethod
    def wants_to_see(app, pwd):
        ...

    def __init__(self):
        self.category = ''
        self.name = ''
        self.form = {}

    def sees_page_interaction(self, request, name):
        self.request = request
        self.category = 'page interaction'
        self.name = name
        self._send_event()

    def sees_form_interaction(self, request):
        self.request = request
        self.category = 'form interaction'
        self.name = "submit"
        self.form = request.POST
        self._send_event()

    def _send_event(self):
        host = self.request.META['HTTP_HOST']
        payload = {
            "session_id": uuid.uuid4().hex,  # TODO: this is wrong!
            "category": self.category,
            "name": self.name,
            "data": {
                "host": host,
                "path": self.request.path_info,
            },
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        }
        if self.name == "cta click":
            payload['data']['element'] = 'chat bubble'
        if self.form:
            payload['data']['form'] = self.form

        requests.post(self.url, json=payload)