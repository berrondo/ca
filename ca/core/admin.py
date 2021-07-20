from django.contrib import admin
from ca.core.models import Event, RawEvent


class MyAdmin:
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class EventAdmin(MyAdmin, admin.ModelAdmin):
    fields = ('session_id', ('category', 'name'), 'data', 'timestamp')
    readonly_fields = ('session_id', 'category', 'name', 'data', 'timestamp')
    search_fields = ('session_id', 'category', 'timestamp')
    list_display = ('session_id', 'category', 'name', 'timestamp')
    list_filter = ('category', 'timestamp')

admin.site.register(Event, EventAdmin)


class RawEventAdmin(MyAdmin, admin.ModelAdmin):
    fields = ('payload', )
    readonly_fields = fields
    list_display = ('created_at', 'status', 'payload')
    list_filter = ('status', 'created_at')

admin.site.register(RawEvent, RawEventAdmin)
