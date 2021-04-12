from django.contrib.gis.db import models
from django.contrib.gis import forms


class Place(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    location = models.PointField()

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)


class PlaceType(models.Model):

    place_type = models.CharField(
        max_length=100, verbose_name='Type of the place')

    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
