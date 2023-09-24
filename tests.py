import unittest
from main import second_level


class TestSecondLevel(unittest.TestCase):
    def test_asc_second_level(self):
        self.assertTrue(second_level([1, 2, 3, 4, 5]))

    def test_desc_second_level(self):
        self.assertTrue(second_level([5, 4, 3, 2, 1]))

    def test_not_monotonous(self):
        self.assertFalse(second_level([1, 2, 2, 3, 2, 4]))


if __name__ == "__main__":
    unittest.main()
