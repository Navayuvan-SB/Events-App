from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event


class EventsListView(LoginRequiredMixin, generic.ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(created_by__exact=self.request.user)


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
