import unittest

from exercise4 import nearest_post_offices


class TestNearestPostOffices(unittest.TestCase):
    def test_expected_offices(self):
        n = 3
        location = [0, 0]
        post_office_locations = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]

        offices = nearest_post_offices(n, location, post_office_locations)
        expected_offices = [[-1, 2], [0, 3], [4, 3]]

        self.assertEqual(len(offices), len(expected_offices))
        for office in expected_offices:
            self.assertTrue(office in offices)
