import unittest

from exercise6 import get_favourite_genres


class TestGetFavouriteGenres(unittest.TestCase):
    def test_expected_results(self):
        users = {
            "David": ["song1", "song2", "song3", "song4", "song8"],
            "Emma": ["song5", "song6", "song7"]
        }

        genres = {
            "Rock": ["song1", "song3"],
            "Dubstep": ["song7"],
            "Techno": ["song2", "song4"],
            "Pop": ["song5", "song6"],
            "Jazz": ["song8", "song9"]
        }

        expected_result = {
           "David": ["Rock", "Techno"],
           "Emma":  ["Pop"]
        }

        result = get_favourite_genres(users, genres)

        self.assertEqual(expected_result, result)
