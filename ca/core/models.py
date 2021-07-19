from django.db import models


class Event(models.Model):
    session_id = models.UUIDField(db_index=True)
    category = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
