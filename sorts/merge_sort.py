# branch_coverage = {
#     "merge_sort_1": False,  
#     "merge_sort_2": False,  
#     "merge_sort_3": False,  
#     "merge_sort_4": False, 
#     "merge_sort_5": False   
# }

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    if length > 1:
        # branch_coverage["merge_sort_1"] = True
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            # branch_coverage["merge_sort_2"] = True
            if left_half[i] < right_half[j]:
                # branch_coverage["merge_sort_3"] = True
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            # branch_coverage["merge_sort_4"] = True
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            # branch_coverage["merge_sort_5"] = True
            collection[k] = right_half[j]
            j += 1
            k += 1

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

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
    # print_coverage()
