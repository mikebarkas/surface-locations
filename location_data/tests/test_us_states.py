from django.test import TestCase

from location_data import us_states


class StateSelectListTest(TestCase):

    def setUp(self):
        self.states_list = us_states.us_states()
        self.abbreviation_name = us_states.state_abbreviation_and_name('nc')

    def test_us_state_select_list(self):
        self.assertTrue(len(self.states_list))

    def test_abbreviation_and_name(self):
        self.assertEqual(('NC', 'North Carolina'), self.abbreviation_name)
