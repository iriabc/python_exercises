import unittest

from exercise7 import moves_to_show_same_number_of_pips

class TestMovesToSameNumberOfPips(unittest.TestCase):
    def test_1(self):
        """
        You can pick the first two dice and rotate each of them in one move so that they all show
        three pips.
        """
        pips = [1, 2, 3]

        result = moves_to_show_same_number_of_pips(pips)

        self.assertEqual(result, 2)

    def test_2(self):
        """
        You can pick the last dice and rotate it in two moves so it shows one pip.
        """
        pips = [1, 1, 6]

        result = moves_to_show_same_number_of_pips(pips)

        self.assertEqual(result, 2)

    def test_3(self):
        """
        You can make all dice show 2 rotating them.
        """
        pips = [1, 6, 2, 3]

        result = moves_to_show_same_number_of_pips(pips)

        self.assertEqual(result, 3)
