from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    actions = None
    fields = ('session_id', ('category', 'name'), 'data', 'timestamp')
    readonly_fields = ('session_id', 'category', 'name', 'data', 'timestamp')
    search_fields = ('session_id', 'category', 'timestamp')
    list_display = ('session_id', 'category', 'name', 'timestamp')
    list_filter = ('category', 'timestamp')


admin.site.register(Event, EventAdmin)
