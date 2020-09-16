import unittest

from exercise5 import longest_vowel_strings


class TestLongestVowelStrings(unittest.TestCase):
    def test_1(self):
        word = "earthproblem"
        s = longest_vowel_strings(word)

        self.assertEqual(s, 3)

    def test_2(self):
        word = "letsgosomewhere"
        s = longest_vowel_strings(word)

        self.assertEqual(s, 2)

    def test_3(self):
        word = "mkmklp"
        s = longest_vowel_strings(word)

        self.assertEqual(s, 0)

    def test_4(self):
        word = "aeioafggfdeg"
        s = longest_vowel_strings(word)

        self.assertEqual(s, 6)

    def test_5(self):
        word = "aaaaaaaa"
        s = longest_vowel_strings(word)

        self.assertEqual(s, 8)
