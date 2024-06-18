import pytest
from merge_sort import merge_sort

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert merge_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]

def test_merge_sort_with_negatives():
    assert merge_sort([-1, -3, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]

def test_merge_sort_duplicates():
    assert merge_sort([3, 1, 2, 3, 2]) == [1, 2, 2, 3, 3]

def test_merge_sort_large_numbers():
    assert merge_sort([1000, 500, 1500, 200, 2500]) == [200, 500, 1000, 1500, 2500]

def test_merge_sort_strings():
    assert merge_sort(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

if __name__ == "__main__":
    pytest.main()
