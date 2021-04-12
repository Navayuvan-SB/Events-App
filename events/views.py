from django.views import generic
from .models import Event


class EventsListView(generic.ListView):
    model = Event


class EventDetailView(generic.DetailView):
    model = Event
