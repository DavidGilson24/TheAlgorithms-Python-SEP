from __future__ import print_function
import math

branchcoverage = {
    "jump_search_1": False,  
    "jump_search_2": False,  
    "jump_search_3": False,
    "jump_search_4": False,
    "jump_search_5": False,
}

def jump_search(arr, x):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n)-1] < x:
        branchcoverage["jump_search_1"] = True
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            branchcoverage["jump_search_2"] = True
            return -1

    while arr[prev] < x:
        branchcoverage["jump_search_3"] = True
        prev = prev + 1
        if prev == min(step, n):
            branchcoverage["jump_search_4"] = True
            return -1

    if arr[prev] == x:
        branchcoverage["jump_search_5"] = True
        return prev

    return -1

def printcoverage():
    total_branches = len(branchcoverage)
    executed_branches = sum(1 for hit in branchcoverage.values() if hit)
    coverage_percentage = (executed_branches / total_branches) * 100

    for branch, hit in branchcoverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print(f"Branch coverage: {coverage_percentage:.2f}%")

def reset_coverage():
    global branchcoverage
    branchcoverage = {
        "jump_search_1": False,
        "jump_search_2": False,
        "jump_search_3": False,
        "jump_search_4": False,
        "jump_search_5": False,
    }

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
reset_coverage()
index = jump_search(arr, x)
print("\nNumber " + str(x) +" is at index " + str(index))
printcoverage()

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 0
reset_coverage()
index = jump_search(arr, x)
print("\nNumber " + str(x) +" is at index " + str(index))
printcoverage()

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 610
reset_coverage()
index = jump_search(arr, x)
print("\nNumber " + str(x) +" is at index " + str(index))
printcoverage()

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 1
reset_coverage()
index = jump_search(arr, x)
print("\nNumber " + str(x) +" is at index " + str(index))
printcoverage()
