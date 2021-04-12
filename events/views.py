from django.views import generic
from .models import Event


class EventsListView(generic.ListView):
    model = Event
