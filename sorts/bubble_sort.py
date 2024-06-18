# branch_coverage = {
#     "bubble_sort_1": False,  
#     "bubble_sort_2": False,  
#     "bubble_sort_3": False,  
#     "bubble_sort_4": False   
# }

def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    length = len(collection)
    for i in range(length-1):
        # branch_coverage["bubble_sort_1"] = True
        swapped = False
        for j in range(length-1-i):
            # branch_coverage["bubble_sort_2"] = True
            if collection[j] > collection[j+1]:
                # branch_coverage["bubble_sort_3"] = True
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped:
            # branch_coverage["bubble_sort_4"] = True
            break  # Stop iteration if the collection is sorted.
    return collection

# def print_coverage():
#     total_branches = len(branch_coverage)
#     taken_branches = sum(1 for taken in branch_coverage.values() if taken)
#     coverage_percentage = (taken_branches / total_branches) * 100
    
#     for branch, hit in branch_coverage.items():
#         print(f"{branch}: {'Taken' if hit else 'Not taken'}")
    
#     print(f"Total Coverage Percentage: {coverage_percentage:.2f}%")

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
    # print_coverage()
