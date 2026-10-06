import unittest

from gradebook.utils import mean, letter_grade


class TestUtils(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([90, 80, 70]), 80)

    def test_letter_grade(self):
        self.assertEqual(letter_grade(90), "A")


if __name__ == "__main__":
    unittest.main()