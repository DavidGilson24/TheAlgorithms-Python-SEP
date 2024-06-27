import unittest
from gnome_sort import gnome_sort
class TestGnomeSort(unittest.TestCase):

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):

        arr = [5, 4, 3, 2, 1]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        gnome_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [1]
        gnome_sort(arr)
        self.assertEqual(arr, [1])

if __name__ == '__main__':
    unittest.main()

