import unittest

from exercise2 import minimum_route_to_treasure


class TestMinimumRouteToTreasure(unittest.TestCase):
    def test_correct_route_1(self):
        the_map = [
            ["O", "O", "O", "O"],
            ["D", "O", "D", "O"],
            ["O", "O", "O", "O"],
            ["X", "D", "D", "O"],
        ]

        result = minimum_route_to_treasure(the_map)
        expected_result = [
            (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0)
        ]

        self.assertEqual(len(result), 6)
        self.assertEqual(result, expected_result)

    def test_correct_route_2(self):
        the_map = [
            ["O", "O", "O"],
            ["D", "O", "D"],
            ["O", "O", "X"],
            ["D", "D", "D"],
        ]

        result = minimum_route_to_treasure(the_map)
        expected_result = [
            (0, 0), (0, 1), (1, 1), (2, 1), (2, 2)
        ]

        self.assertEqual(len(result), 5)
        self.assertEqual(result, expected_result)
