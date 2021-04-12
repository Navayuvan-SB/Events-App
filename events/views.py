from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event


class EventsListView(LoginRequiredMixin, generic.ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(created_by__exact=self.request.user)


class EventDetailView(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = Event

    def test_func(self):
        id = self.kwargs['pk']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by
