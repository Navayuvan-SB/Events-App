from django.db import models
from model_utils.models import TimeStampedModel
from place.models import Place
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Event(TimeStampedModel):

    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    tags = TaggableManager()


class EventTime(models.Model):

    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)

    all_day = models.BooleanField()

    from_time = models.DateTimeField(
        verbose_name='start time of the event', default=None)
    end_time = models.DateTimeField(
        verbose_name='end time of the event', default=None)
