import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_full_binary_tree(tree):
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        return False

@pytest.fixture
def sample_tree():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    return tree

# Branch 1: tree is None
def test_is_full_binary_tree_none():
    assert is_full_binary_tree(None) == True

# Branch 2: tree has no children
def test_is_full_binary_tree_no_children():
    tree = Node(1)
    assert is_full_binary_tree(tree) == True

# Branch 3.1: tree has left child and right child
def test_is_full_binary_tree_left_right_child():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    assert is_full_binary_tree(tree) == True

# Branch 3.2: tree has left child only
def test_is_full_binary_tree_left_child():
    tree = Node(1)
    tree.left = Node(2)
    assert is_full_binary_tree(tree) == False

# Branch 3.3: tree has right child only
def test_is_full_binary_tree_right_child():
    tree = Node(1)
    tree.right = Node(2)
    assert is_full_binary_tree(tree) == False

# Just a extra tree to test if it is a full binary tree
def test_complex_tree(sample_tree):
    assert is_full_binary_tree(sample_tree) == False

if __name__ == '__main__':
    pytest.main()


