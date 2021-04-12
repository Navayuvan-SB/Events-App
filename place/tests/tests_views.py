from django.test import TestCase
from django.urls import reverse

from django.contrib.gis.geos import Point

from place.models import Place, PlaceType


class PlaceListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_places = 15
        for place_id in range(number_of_places):

            place_type_1 = PlaceType.objects.create(place_type="Tourism")
            place_type_2 = PlaceType.objects.create(place_type="Metropolitan")

            test_place = Place.objects.create(title=f'Place {place_id}', description="Sample description",
                                              address="Sample address", city="Sample city", location=Point(100, 102))

            test_place.placetype_set.add(place_type_1)
            test_place.placetype_set.add(place_type_2)

            test_place.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/place/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('places'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('places'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place/place_list.html')


class PlaceDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        place_type_1 = PlaceType.objects.create(place_type="Tourism")
        place_type_2 = PlaceType.objects.create(place_type="Metropolitan")

        test_place = Place.objects.create(pk=1,title=f'Place Sample', description="Sample description",
                                            address="Sample address", city="Sample city", location=Point(100, 102))

        test_place.placetype_set.add(place_type_1)
        test_place.placetype_set.add(place_type_2)

        test_place.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/place/1')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('place-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('place-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place/place_detail.html')

    def test_return_HTTP404_if_blog_not_found(self):
        response = self.client.get(reverse('place-detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 404)
