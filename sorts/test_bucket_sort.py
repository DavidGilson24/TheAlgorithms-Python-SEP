import pytest
from bucket_sort import bucketSort,  DEFAULT_BUCKET_SIZE

class TestBucketSort:
    def bucketSortEmptyListCheck(self, myList, bucketSize = DEFAULT_BUCKET_SIZE):
        if len(myList) == 0:
            # coverage["bucketSort1"] = True
            print('empty array')
            return []
        return bucketSort(myList, bucketSize)

    def testBucketSortEmptyList(self):
        sortedArray = self.bucketSortEmptyListCheck([])
        assert sortedArray == []
        # printCoverage()

    def testBucketSortSingleBucket(self):
        sortedArray = self.bucketSortEmptyListCheck([9, 7, 5, 3])
        assert sortedArray == [3, 5, 7, 9]
        # printCoverage()

    def testBucketSortMultipleBuckets(self):
        sortedArray = self.bucketSortEmptyListCheck([15, 23, 4, 8, 3, 2, 17, 11, 6, 19])
        assert sortedArray == [2, 3, 4, 6, 8, 11, 15, 17, 19, 23]
        # printCoverage()

    def testBucketSortSame(self):
        sortedArray = self.bucketSortEmptyListCheck([2, 2, 2, 2])
        assert sortedArray == [2, 2, 2, 2]
        # printCoverage()

    def testBucketSortAlreadySorted(self):
        sortedArray = self.bucketSortEmptyListCheck([1, 3, 5, 7, 9])
        assert sortedArray == [1, 3, 5, 7, 9]
        # printCoverage()

    def testBucketSortNegativeValues(self):
        sortedArray = self.bucketSortEmptyListCheck([-5, -3, -7, -1])
        assert sortedArray == [-7, -5, -3, -1]
        # printCoverage()

if __name__ == '__main__':
    pytest.main()
