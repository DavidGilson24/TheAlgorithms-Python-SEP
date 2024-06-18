import pytest
from binary_search import binary_search

class TestBinarySearch:
    def setup_method(self):
        self.collection = [0, 5, 7, 10, 15]
    
    def testBinarySearchEmptyCollection(self):
        assert binary_search([], 0) == None

    def testBinarySearchFirstElement(self):
        assert binary_search(self.collection, 0) == 0

    def testBinarySearchLastElement(self):
        assert binary_search(self.collection, 15) == 4
    
    def testBinarySearchMiddleElement(self):
        assert binary_search(self.collection, 5) == 1
    
    def testBinarySearchElementNotInCollection(self):
        assert binary_search(self.collection, 6) == None

if __name__ == '__main__':
    pytest.main()