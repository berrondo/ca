from django.db import models


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
