from django.contrib import admin
from .models import Event, EventTime


class EventTimeInlineAdmin(admin.TabularInline):
    model = EventTime
    fields = ['event_date', 'from_time', 'end_time', 'all_day']
    extra = 2


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')
    inlines = [EventTimeInlineAdmin]
