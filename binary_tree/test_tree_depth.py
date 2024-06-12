import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth_of_tree(tree):
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree

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
def test_depth_of_tree_none():
    assert depth_of_tree(None) == 0

# Branch 2.1: depth_l_tree > depth_r_tree
def test_depth_l_tree_greater():
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(3)
    assert depth_of_tree(tree) == 3

# Branch 2.2: depth_l_tree <= depth_r_tree
def test_depth_r_tree_greater():
    tree = Node(1)
    tree.right = Node(2)
    tree.right.right = Node(3)
    assert depth_of_tree(tree) == 3

# Branch 2.3: balanced tree (depth_l_tree == depth_r_tree)
def test_balanced_tree():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    assert depth_of_tree(tree) == 2

# Just a extra tree to test the depth
def test_complex_tree(sample_tree):
    assert depth_of_tree(sample_tree) == 5


if __name__ == '__main__':
    pytest.main()
