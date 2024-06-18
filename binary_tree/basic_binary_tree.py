# ===================================================================================USED FOR COVERAGE INSTRUMENTATION================================================================================================
# branch_coverage = {
#     "depthOfTree1": False,  
#     "depthOfTree2": False, 
#     "depthOfTree3": False,  
#     "isFullBinary1": False,  
#     "isFullBinary2": False,  
#     "isFullBinary3": False, 
#     "isFullBinary4": False,  
# }
# ================================================================================================================================================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_of_tree(tree):
    if tree is None:
        # branch_coverage["depthOfTree1"] = True
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            # branch_coverage["depthOfTree2"] = True
            return 1 + depth_l_tree
        else:
            # branch_coverage["depthOfTree3"] = True
            return 1 + depth_r_tree


def is_full_binary_tree(tree):
    if tree is None:
        # branch_coverage["isFullBinary1"] = True
        return True
    if (tree.left is None) and (tree.right is None):
        # branch_coverage["isFullBinary2"] = True
        return True
    if (tree.left is not None) and (tree.right is not None):
        # branch_coverage["isFullBinary3"] = True
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        # branch_coverage["isFullBinary4"] = True
        return False

# =================================================================================USED FOR COVERAGE INSTRUMENTATION================================================================================================
# def print_coverage():
#     total_branches = len(branch_coverage)
#     taken_branches = sum(taken for taken in branch_coverage.values())
#     coverage_percentage = (taken_branches / total_branches) * 100

#     for branch, taken in branch_coverage.items():
#         print(f"{branch}: {'Taken' if taken else 'Not taken'}")
    
#     print(f"Total Coverage Percentage: {coverage_percentage:.2f}%")
# ================================================================================================================================================================================================================

def main():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))

# =================================================================================USED FOR COVERAGE INSTRUMENTATION================================================================================================
    # # Test 1
    # tree1 = Node(1)
    # tree1.left = Node(2)
    # tree1.right = Node(3)
    # print("=====Test 1=====")
    # print(f"Is Full Binary Tree?: {is_full_binary_tree(tree1)}")
    # print(f"Depth of tree: {depth_of_tree(tree1)}")
    # print_coverage()
    # print("=====End of Test 1=====\n")

    # for key in branch_coverage:
    #     branch_coverage[key] = False

    # # Test 2
    # tree2 = Node(1)
    # tree2.left = Node(2)
    # tree2.left.left = Node(3)
    # print("=====Test 2=====")
    # print(f"Is Full Binary Tree?: {is_full_binary_tree(tree2)}")
    # print(f"Depth of tree: {depth_of_tree(tree2)}")
    # print_coverage()
    # print("=====End of Test 2=====\n")

    # for key in branch_coverage:
    #     branch_coverage[key] = False
    
    # #Test 3
    # tree3 = None
    # print("=====Test 3======")
    # print(f"Is Full Binary Tree?: {is_full_binary_tree(tree3)}")
    # print(f"Depth of tree: {depth_of_tree(tree3)}")
    # print_coverage()
    # print("=====End of Test 3=====\n")

    # for key in branch_coverage:
    #     branch_coverage[key] = False

    # # Test 4
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.left.left = Node(4)
    # tree.left.right = Node(5)
    # tree.left.right.left = Node(6)
    # tree.right.left = Node(7)
    # tree.right.left.left = Node(8)
    # tree.right.left.left.right = Node(9)
    # print("=====Test 4=====")
    # print(f"Is Full Binary Tree?: {is_full_binary_tree(tree)}")
    # print(f"Depth of tree: {depth_of_tree(tree)}")
    # print_coverage()
    # print("=====End of Test 4=====\n")
# ================================================================================================================================================================================================================ 

if __name__ == '__main__':
    main()


