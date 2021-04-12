from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place, PlaceType


class PlaceTypeInlineAdmin(admin.TabularInline):
    model = PlaceType
    extra = 2


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')
    inlines = [PlaceTypeInlineAdmin]
