import unittest
from main_task import square_board


class TestSquareBoard(unittest.TestCase):

    def test_example_1(self):
        number, width, height = 10, 2, 3
        self.assertEqual(square_board(number, width, height), 9)

    def test_example_2(self):
        number, width, height = 2, 1000000000, 999999999
        self.assertEqual(square_board(number, width, height), 1999999998)

    def test_example_3(self):
        number, width, height = 4, 1, 1
        self.assertEqual(square_board(number, width, height), 2)


if __name__ == '__main__':
    unittest.main()
