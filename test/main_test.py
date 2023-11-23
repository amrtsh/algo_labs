import os
import unittest
from unittest.mock import patch
from io import StringIO
from src.min_beer import read_input, is_valid, create_matrix, transpose_matrix, find_y_indexes, generate_combinations, \
    find_beer_solution


class TestBeerPartySolver(unittest.TestCase):
    def setUp(self):
        self.input_file_content = "5 5\nYNNNY YYNNY NYYNY NNYYY NNNYN"
        self.input_file_path = "test_input.txt"
        with open(self.input_file_path, 'w') as f:
            f.write(self.input_file_content)

    def tearDown(self):
        # Clean up the test input file
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)

    def test_read_input(self):
        num_of_employees, amount_of_beer_available, y_or_n = read_input(self.input_file_path)
        self.assertEqual(num_of_employees, 5)
        self.assertEqual(amount_of_beer_available, 5)
        self.assertEqual(y_or_n, ['YNNNY', 'YYNNY', 'NYYNY', 'NNYYY', 'NNNYN'])

    def test_is_valid(self):
        self.assertTrue(is_valid(5, 10))
        self.assertFalse(is_valid(0, 10))
        self.assertFalse(is_valid(5, -1))
        self.assertFalse(is_valid(55, 10))

    def test_create_matrix(self):
        matrix = create_matrix(['YNNNY', 'YYNNY', 'NYYNY', 'NNYYY', 'NNNYN'])
        self.assertEqual(matrix, [['Y', 'N', 'N', 'N', 'Y'], ['Y', 'Y', 'N', 'N', 'Y'], ['N', 'Y', 'Y', 'N', 'Y'],
                                  ['N', 'N', 'Y', 'Y', 'Y'], ['N', 'N', 'N', 'Y', 'N']])

    def test_transpose_matrix(self):
        matrix = [['Y', 'N', 'N', 'N', 'Y'], ['Y', 'Y', 'N', 'N', 'Y'], ['N', 'Y', 'Y', 'N', 'Y'],
                  ['N', 'N', 'Y', 'Y', 'Y'], ['N', 'N', 'N', 'Y', 'N']]
        transposed_matrix = transpose_matrix(matrix)
        self.assertEqual(transposed_matrix,
                         [['Y', 'Y', 'N', 'N', 'N'], ['N', 'Y', 'Y', 'N', 'N'], ['N', 'N', 'Y', 'Y', 'N'],
                          ['N', 'N', 'N', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'N']])

    def test_find_y_indexes(self):
        result_matrix = [['Y', 'Y', 'N', 'N', 'N'], ['N', 'Y', 'Y', 'N', 'N'], ['N', 'N', 'Y', 'Y', 'N'], ['N', 'N', 'N', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'N']]
        y_indexes = find_y_indexes(result_matrix)
        self.assertEqual(y_indexes, {0: [0, 1], 1: [1, 2], 2: [2, 3], 3: [3, 4], 4: [0, 1, 2, 3]})

    @patch('sys.stdout', new_callable=StringIO)
    def test_find_beer_solution(self, mock_stdout):
        y_indexes = {0: [0, 1], 1: [1, 2], 2: [2, 3], 3: [3, 4], 4: [0, 1, 2, 3]}
        find_beer_solution(y_indexes, 5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Rows: [3, 4]")


if __name__ == '__main__':
    unittest.main()
