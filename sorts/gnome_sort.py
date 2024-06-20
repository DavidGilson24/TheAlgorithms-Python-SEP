from __future__ import print_function
# branch_coverage = {
#     "gnome_sort_1": False,  
#     "gnome_sort_2": False,  
#     "gnome_sort_3": False,
#     "gnome_sort_4": False,
#     "gnome_sort_5": False 
# }

def gnome_sort(unsorted):
    """
    Pure implementation of the gnome sort algorithm in Python.
    """
    if len(unsorted) <= 1:
        # branch_coverage["gnome_sort_1"] = True
        return unsorted
        
    i = 1
    
    while i < len(unsorted):
        # branch_coverage["gnome_sort_2"] = True
        if unsorted[i-1] <= unsorted[i]:
            # branch_coverage["gnome_sort_3"] = True
            i += 1
        else:
            # branch_coverage["gnome_sort_4"] = True
            unsorted[i-1], unsorted[i] = unsorted[i], unsorted[i-1]
            i -= 1
            if (i == 0):
                # branch_coverage["gnome_sort_5"] = True
                i = 1

# def printCoverage():
#     total_branches = len(branch_coverage)
#     executed_branches = sum(1 for hit in branch_coverage.values() if hit)
#     coverage_percentage = (executed_branches / total_branches) * 100

#     for branch, hit in branch_coverage.items():
#         print(f"{branch} was {'hit' if hit else 'not hit'}")

#     print(f"Branch coverage: {coverage_percentage:.2f}%")

if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    gnome_sort(unsorted)
    print(unsorted)
    # printCoverage()
