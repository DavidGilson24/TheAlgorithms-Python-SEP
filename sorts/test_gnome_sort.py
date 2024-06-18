import unittest
from gnome_sort import gnome_sort, branch_coverage
class TestGnomeSort(unittest.TestCase):

    def test_already_sorted(self):
        global branch_coverage
        arr = [1, 2, 3, 4, 5]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(branch_coverage["gnome_sort_2"])
        self.assertTrue(branch_coverage["gnome_sort_3"])
        self.assertFalse(branch_coverage["gnome_sort_4"])

    def test_reverse_sorted(self):
        global branch_coverage
        arr = [5, 4, 3, 2, 1]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(branch_coverage["gnome_sort_2"])
        self.assertTrue(branch_coverage["gnome_sort_3"])
        self.assertTrue(branch_coverage["gnome_sort_4"])

    def test_empty_array(self):
        global branch_coverage
        arr = []
        gnome_sort(arr)
        self.assertEqual(arr, [])
        self.assertTrue(branch_coverage["gnome_sort_1"])

    def test_single_element(self):
        global branch_coverage
        arr = [1]
        gnome_sort(arr)
        self.assertEqual(arr, [1])
        self.assertTrue(branch_coverage["gnome_sort_1"])

if __name__ == '__main__':
    unittest.main()

