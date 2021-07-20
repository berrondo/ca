from django.db import models


class Event(models.Model):
    session_id = models.UUIDField(db_index=True)
    category = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['session_id', 'timestamp']


class RawEvent(models.Model):
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Status(models.IntegerChoices):
        RECEIVED = 0
        PROCESSED = 1
        INVALID = 2
    status = models.IntegerField(choices=Status.choices, default=Status.RECEIVED)

    class Meta:
        ordering = ['-created_at']