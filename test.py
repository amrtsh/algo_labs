import unittest

from main import bfs, is_valid


class TestBFS(unittest.TestCase):

    def test_valid_path(self):
        N = 8
        start_x, start_y = 0, 0
        end_x, end_y = 1, 2
        shortest_path = bfs(start_x, start_y, end_x, end_y, N)
        self.assertEqual(shortest_path, 1)

    def test_invalid_path(self):
        N = 3
        start_x, start_y = 1, 1
        end_x, end_y = 0, 0
        shortest_path = bfs(start_x, start_y, end_x, end_y, N)
        self.assertEqual(shortest_path, -1)

    def test_is_valid(self):
        N = 8
        self.assertTrue(is_valid(0, 0, N))
        self.assertTrue(is_valid(7, 7, N))
        self.assertFalse(is_valid(-1, 0, N))
        self.assertFalse(is_valid(0, 8, N))


if __name__ == '__main__':
    unittest.main()
