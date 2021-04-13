import django_filters
from django import forms
from .models import Event, EventTime


class DateInput(forms.DateInput):
    input_type = 'date'


class EventFilter(django_filters.FilterSet):

    DATES = tuple((x, x) for x in range(1, 32))

    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )

    date = django_filters.ChoiceFilter(
        label='Event Date', method='filter_by_date', choices=DATES)

    month = django_filters.ChoiceFilter(
        label='Event Month', method='filter_by_month', choices=MONTHS)

    year = django_filters.NumberFilter(
        label='Event Year', method='filter_by_year')

    class Meta:
        model = Event
        fields = {
            'title': ['icontains'],
        }

    def filter_by_date(self, queryset, name, value):
        eventtime_ids = EventTime.objects.filter(
            event_date__day=value).values_list('event_id', flat=True)
        return queryset.filter(id__in=eventtime_ids)

    def filter_by_month(self, queryset, name, value):
        eventtime_ids = EventTime.objects.filter(
            event_date__month=value).values_list('event_id', flat=True)
        return queryset.filter(id__in=eventtime_ids)

    def filter_by_year(self, queryset, name, value):
        eventtime_ids = EventTime.objects.filter(
            event_date__year=value).values_list('event_id', flat=True)
        return queryset.filter(id__in=eventtime_ids)
