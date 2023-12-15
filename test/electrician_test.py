import unittest

from src.electrician import set_distance


class TestSetDistance(unittest.TestCase):

    def test_case_1(self):
        distance = 2
        height_of_pillar = [3, 3, 3]
        result = set_distance(distance, height_of_pillar)
        self.assertAlmostEqual(result, 5.66, places=2)

    def test_case_2(self):
        distance = 100
        height_of_pillar = [1, 1, 1, 1]
        result = set_distance(distance, height_of_pillar)
        self.assertAlmostEqual(result, 300, places=2)

    def test_case_3(self):
        distance = 4
        height_of_pillar = [100, 2, 100, 2, 100]
        result = set_distance(distance, height_of_pillar)
        self.assertAlmostEqual(result, 396.32, places=2)


if __name__ == '__main__':
    unittest.main()
