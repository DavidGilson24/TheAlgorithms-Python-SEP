import pytest
from interpolation_search import interpolation_search, printCoverage, coverage

class TestInterpolationSearch:
    def setup_method(self):
        self.collection = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    def test_interpolationSearchEmptyList(self):
        result = interpolation_search([], 10)
        assert result is None
        coverage["interpolationSearch1"] = True
        printCoverage()

    def test_interpolationSearchExistingMiddle(self):
        result = interpolation_search(self.collection, 23)
        assert result == 5
        printCoverage()

    def test_interpolationSearchExistingFirst(self):
        result = interpolation_search(self.collection, 2)
        assert result == 0
        printCoverage()

    def test_interpolationSearchExistingLast(self):
        result = interpolation_search(self.collection, 91)
        assert result == 9
        printCoverage()

    def test_interpolationSearchNonExisting(self):
        collection = [1, 2, 3, 4, 5]
        result = interpolation_search(collection, 6)
        assert result is None
        printCoverage()

    def test_interpolationSearchOutOfRange(self):
        collection = [10, 20, 30, 40]
        result = interpolation_search(collection, 50)
        assert result is None
        printCoverage()

if __name__ == '__main__':
    pytest.main()
