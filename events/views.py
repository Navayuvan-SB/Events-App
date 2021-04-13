from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event, EventTime
from django.urls import reverse
from django.contrib.auth.models import User


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


class EventCreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    fields = ('title', 'tags', 'place')
    template_name = "events/event_form.html"

    def form_valid(self, form):

        user = User.objects.get(username=self.request.user.username)

        form.instance.created_by = user

        return super(EventCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse("add-event-timings", kwargs={'pk': self.object.pk})


class EventEditView(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Event
    fields = ('title', 'tags', 'place')
    template_name = "events/event_form.html"

    def test_func(self):
        id = self.kwargs['pk']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by

    def get_success_url(self, **kwargs):
        return reverse("event-detail", kwargs={'pk': self.kwargs['pk']})


class EventTimeCreateView(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = EventTime
    fields = ('event_date', 'all_day', 'from_time', 'end_time')
    template_name = "events/event_time_form.html"

    def test_func(self):
        id = self.kwargs['pk']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by

    def form_valid(self, form):
        event = Event.objects.get(pk=self.kwargs['pk'])
        form.instance.event = event
        form.save()
        return super(EventTimeCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):

        if self.request.method == 'POST' and 'next' in self.request.POST:
            return reverse("add-event-timings", kwargs={'pk': self.kwargs['pk']})

        elif self.request.method == 'POST' and 'final' in self.request.POST:
            return reverse("events")


class EventTimeEditView(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = EventTime
    fields = ('event_date', 'all_day', 'from_time', 'end_time')
    template_name = "events/event_time_form.html"

    def test_func(self):
        id = self.kwargs['eventid']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_request_from_update'] = True
        return context

    def get_success_url(self, **kwargs):
        return reverse("event-detail", kwargs={'pk': self.kwargs['eventid']})


class EventDeleteView(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):

    model = Event
    template_name = "events/event_delete.html"

    def test_func(self):
        id = self.kwargs['pk']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by

    def get_success_url(self, **kwargs):
        return reverse("events")


class EventTimeDeleteView(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = EventTime
    template_name = "events/event_time_delete.html"

    def test_func(self):
        id = self.kwargs['eventid']
        user_event = Event.objects.get(pk=id)
        return self.request.user == user_event.created_by

    def get_success_url(self, **kwargs):
        return reverse("event-detail", kwargs={'pk': self.kwargs['eventid']})
