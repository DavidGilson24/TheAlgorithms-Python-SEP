#!/usr/bin/env python
# Author: OMKAR PATHAK
# This program will illustrate how to implement bucket sort algorithm

# Wikipedia says: Bucket sort, or bin sort, is a sorting algorithm that works by distributing the
# elements of an array into a number of buckets. Each bucket is then sorted individually, either using
# a different sorting algorithm, or by recursively applying the bucket sorting algorithm. It is a
# distribution sort, and is a cousin of radix sort in the most to least significant digit flavour.
# Bucket sort is a generalization of pigeonhole sort. Bucket sort can be implemented with comparisons
# and therefore can also be considered a comparison sort algorithm. The computational complexity estimates
# involve the number of buckets.

#  Time Complexity of Solution:
#  Best Case O(n); Average Case O(n); Worst Case O(n)

from __future__ import print_function
from insertion_sort import insertion_sort
import math

DEFAULT_BUCKET_SIZE = 5

coverage = {
    "bucketSort1": False,
    "bucketSort2": False,
    "bucketSort3": False,
    "bucketSort4": False,
    "bucketSort5": False,
    "bucketSort6": False,
    "bucketSort7": False,
    "bucketSort8": False,
}

def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    if(len(myList) == 0):
        coverage["bucketSort1"] = True
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        coverage["bucketSort2"] = True
        if myList[i] < minValue:
            coverage["bucketSort3"] = True
            minValue = myList[i]
        elif myList[i] > maxValue:
            coverage["bucketSort4"] = True
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        coverage["bucketSort5"] = True
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        coverage["bucketSort6"] = True
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        coverage["bucketSort7"] = True
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            coverage["bucketSort8"] = True
            sortedArray.append(buckets[i][j])

    return sortedArray

def printCoverage():
    totalBranches = len(coverage)
    executedBranches = sum(1 for hit in coverage.values() if hit)
    coveragePercentage = (executedBranches / totalBranches) * 100

    for branch, hit in coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print(f"Branch coverage: {coveragePercentage:.2f}%")


if __name__ == '__main__':
    sortedArray = bucketSort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sortedArray)
    
    print('more solutions:')

    print('Test 1 single bucket:')
    sortedArray = bucketSort([9, 7, 5, 3])
    print(sortedArray)
    printCoverage()

    print('Test 2 multiple buckets:')
    sortedArray = bucketSort([15, 23, 4, 8, 3, 2, 17, 11, 6, 19])
    print(sortedArray)
    printCoverage()

    print('Test 3 same numbers:')
    sortedArray = bucketSort([2, 2, 2, 2])
    print(sortedArray)
    printCoverage()

    print('Test 4 already sorted:')
    sortedArray = bucketSort([1, 3, 5, 7, 9])
    print(sortedArray)
    printCoverage()
