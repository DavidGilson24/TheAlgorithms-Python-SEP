import pytest
from bubble_sort import bubble_sort  

def test_bubble_sort_empty():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_unsorted():
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]

def test_bubble_sort_with_negatives():
    assert bubble_sort([-1, -3, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]

def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 2, 3, 2]) == [1, 2, 2, 3, 3]

def test_bubble_sort_large_numbers():
    assert bubble_sort([1000, 500, 1500, 200, 2500]) == [200, 500, 1000, 1500, 2500]

def test_bubble_sort_strings():
    assert bubble_sort(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

if __name__ == "__main__":
    pytest.main()
