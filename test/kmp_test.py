import unittest

from src.kmp_algorithm import find_lps, kmp_search


class TestKMPSearch(unittest.TestCase):
    def test_kmp_search(self):
        # Test Case 1
        haystack = "AABAACAADAABAABA"
        needle = "AABA"
        result = kmp_search(haystack, needle)
        expected = [(0, 3), (9, 12), (12, 15)]
        self.assertEqual(result, expected)

        # Test Case 2
        haystack = "ababcabababc"
        needle = "abab"
        result = kmp_search(haystack, needle)
        expected = [(0, 3), (5, 8), (7, 10)]
        self.assertEqual(result, expected)

    def test_find_lps(self):
        # Test Case for find_lps function
        needle = "AABA"
        M = len(needle)
        lps = [0] * M
        find_lps(needle, M, lps)
        expected_lps = [0, 1, 0, 1]
        self.assertEqual(lps, expected_lps)


if __name__ == '__main__':
    unittest.main()
