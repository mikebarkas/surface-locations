from django.test import TestCase
from django.core.urlresolvers import resolve

from location_data.views import StateSelect, city_list


class StateSelectUrlTest(TestCase):

    def setUp(self):
        self.url = resolve('/state/')

    def test_state_list_url_class(self):
        self.assertEqual(self.url.func.__name__, StateSelect.__name__)

    def test_state_list_url_name(self):
        self.assertEqual(self.url.url_name, 'state-select')


class CityListUrlTest(TestCase):

    def setUp(self):
        self.url = resolve('/state/me/')

    def test_city_list_url_function(self):
        self.assertEqual(self.url.func, city_list)

    def test_city_list_url_name(self):
        self.assertEqual(self.url.url_name, 'city-list')
