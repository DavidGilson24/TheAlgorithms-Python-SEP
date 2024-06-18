from jump_search import jump_search, branchcoverage, reset_coverage
import unittest

class TestJumpSearch(unittest.TestCase):

    def test_found(self):
        global branchcoverage
        arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
        x = 55
        self.assertEqual(jump_search(arr, x), 10)
        self.assertTrue(branchcoverage["jump_search_1"])
        self.assertTrue(branchcoverage["jump_search_5"])

    def test_not_found(self):
        global branchcoverage
        arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
        x = 1000
        self.assertEqual(jump_search(arr, x), -1)
        self.assertTrue(branchcoverage["jump_search_1"])
        self.assertTrue(branchcoverage["jump_search_2"])


if __name__ == '__main__':
    unittest.main()
