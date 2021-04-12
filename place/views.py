from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.urls import reverse

from django.contrib.gis.geos import Point

from .models import Place, PlaceType


class PlaceListView(generic.ListView):
    model = Place


class PlaceDetailView(generic.DetailView):
    model = Place


class PlaceTypeInline(InlineFormSetFactory):
    model = PlaceType
    fields = ['place_type']
    factory_kwargs = {'extra': 2, 'max_num': None,
                      'can_order': False, 'can_delete': False}


class AddPlaceView(CreateWithInlinesView):
    # form_class = PlaceForm
    model = Place
    template_name = 'place/place_form.html'
    fields = ('__all__')
    inlines = [PlaceTypeInline]

    def form_valid(self, form):
        form.instance.location = form.cleaned_data['location']
        return super(AddPlaceView, self).form_valid(form)

    def get_success_url(self):
        return reverse('places')


class EditPlaceView(UpdateWithInlinesView):
    # form_class = PlaceForm
    model = Place
    template_name = 'place/place_form.html'
    fields = ('__all__')
    inlines = [PlaceTypeInline]

    def form_valid(self, form):
        form.instance.location = form.cleaned_data['location']
        return super(EditPlaceView, self).form_valid(form)

    def get_success_url(self):
        return reverse('places')


class DeletePlaceView(DeleteView):
    model = Place

    def get_success_url(self):
        return reverse('places')
