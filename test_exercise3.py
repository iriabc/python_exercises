import unittest

from exercise3 import min_route_to_many_treasures


class TestMinimumRouteToTreasure(unittest.TestCase):
    def test_correct_route_1(self):
        the_map = [
            ["S", "O", "O", "S", "S"],
            ["D", "O", "D", "O", "D"],
            ["O", "O", "O", "O", "X"],
            ["X", "D", "D", "O", "O"],
            ["X", "D", "D", "D", "O"],
        ]

        result = min_route_to_many_treasures(the_map)
        expected_result = [
            (0, 3), (1, 3), (2, 3), (2, 4)
        ]

        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)
