import unittest

from exercise1 import select_movies_pair


class TestSelectMoviesPair(unittest.TestCase):
    def test_select_correct_movies(self):
        movie_duration = [90, 85, 75, 60, 120, 150, 125]
        flight_duration = 250

        movies = select_movies_pair(movie_duration, flight_duration)

        self.assertEqual(movies, (90, 125))

    def test_select_many_movies(self):
        movie_duration = [90, 125, 80, 115]
        flight_duration = 250

        movies = select_movies_pair(movie_duration, flight_duration)

        self.assertEqual(movies, (90, 125))

    def test_no_movies_match_conditions(self):
        movie_duration = [200, 100, 300, 240]
        flight_duration = 250

        with self.assertRaises(ValueError):
            select_movies_pair(movie_duration, flight_duration)

