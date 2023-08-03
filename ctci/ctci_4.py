# CTCI Chapter 4, Trees and Graphs
from typing import Any, List, Optional


class BinaryTreeNode:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<BinaryTreeNode data={self.data} left={self.left.data} right={self.right.data}>"


class TreeNode:
    def __init__(self, data: Any):
        self.data = data
        self.children = []

    def __repr__(self):
        return f"<TreeNode data={self.data} children={self.children}>"


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def dfs(self, target: Any, priority: str = "left") -> Optional[BinaryTreeNode]:
        to_search = [self.root]
        while to_search:
            current = to_search.pop()
            if current:
                print(current.data)
                if target == current.data:
                    return current
                if priority == "left":
                    to_search.extend([current.right, current.left])
                else:
                    to_search.extend([current.left, current.right])
        return None

    def bfs(self, target: Any, priority: str = "left") -> Optional[BinaryTreeNode]:
        to_search = [self.root]
        while to_search:
            current = to_search.pop(0)
            if current:
                print(current.data)
                if target == current.data:
                    return current
                if priority == "left":
                    to_search.extend([current.left, current.right])
                else:
                    to_search.extend([current.right, current.left])
        return None


def traverse(node: BinaryTreeNode, order: str = "in-order") -> None:
    """Traverse in the given order.

    :args:
    order: "in-order" (left, current, right), "pre-order" (current, left, right), "post-order"(left, right, current)

    :return: None
    """
    if node:
        if order == "pre-order":
            print(node.data)
        traverse(node.left, order)
        if order == "in-order":
            print(node.data)
        traverse(node.right, order)
        if order == "post-order":
            print(node.data)


class HeapNode:
    def __init__(self, value: int):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class Heap:
    def __init__(self, root: BinaryTreeNode):
        self.root = root
        self.end = root.left

    def insert(self, value: int) -> None:
        new_node = HeapNode(value)


# 4.2 sorted array to BST
"""
[a, b, c, d, e, f, g] len = 7 max_i = 6 mid = 3
       d
  b         f
a   c     e   g

[a, b, c, d, e, f] len = 6 max_i = 5 mid = 3
       d
  b         f
a   c     e

recursively: get the midpoint (len // 2) and make that the root
get the lower midpoint and make that the left child
get the upper midpoint and make that the right child
pass list slices if we care more about readability than runtime, otherwise use pointers
base case:
"""


# def convert_sorted_list_to_bst(nums: List[int]) -> BinaryTreeNode:
#     upper_bound = len(nums) - 1
#     lower_bound = 0
#     midpoint = len(nums) // 2
#     current = root = BinaryTreeNode(nums[midpoint])
#     upper_midpoint = (upper_bound - midpoint) // 2 + 1
#     lower_midpoint = (midpoint - lower_bound) // 2
#     while upper_midpoint < upper_bound and lower_midpoint > lower_bound:
#         current.left = BinaryTreeNode(nums[lower_midpoint])
#         current.right = BinaryTreeNode(nums[upper_midpoint])
#         upper_midpoint = (upper_bound - midpoint) // 2 + 1
#         lower_midpoint = (midpoint - lower_bound) // 2
#
#     return root

def recursive_make_bst(nums: List[int]) -> Optional[BinaryTreeNode]:
    if not nums:
        return

    midpoint = len(nums) // 2
    node = BinaryTreeNode(nums[midpoint])
    node.left = recursive_make_bst(nums[:midpoint])
    node.right = recursive_make_bst(nums[midpoint + 1:])
    return node


# 4.3 linked list of tree depths
"""
       1
   2       5
 3   4   6   7
 
ll1: 1 -> None
ll2: 2 -> 5
113: 3 -> 4 -> 6 -> 7

uh...no idea. 
make root node a LL then, recursively:
for each node, make its children a LL
store the heads + tails and then combine? how do we keep track of who goes where?

def recursive_ll(parent):
    ...
    return recursive_ll(parent.left) + recursive_ll(parent.right)

BFS -> iterative with a queue is simple
keep track of the value of the node and its level

"""

# 4.4 check balanced
"""
    a
  b       -> False
c
    a
  b   c   -> True
d

if a node has grandchildren on both sides: continue

def is_balanced(node):
    if node.left and node.right:
        return is_balanced(node.left) and is_balanced(node.right)
    elif node.left is None and node.right is None:
        return True
    else:
        if node.left:
            return node.left.left is None and node.left.right is None
        else:
            return node.right.left is None and node.right.right is None
"""

# 4.5 check if BST
"""
def is_bst(node):
    if node.left is None or node.right is None:
        if node.left:
            return node.left < node
        if node.right:
            return node < node.right
        return True
    elif not node.left < node < node.right:
        return False
    else:
        return is_bst(node.left) and is_bst(node.right)
"""

# 4.6 BST successor
"""
       4
   2       6
 1   3   5   7
if node has a right child, its right child's left child's...child is the successor
if node d/n have a right child:
    if node was a left child, its successor is its parent
    if node was a right child:
        if parent was a left child, successor is parent's parent
        if parent was a right child:
        ...repeat recursively. not exactly sure how to do this one
"""

# 4.7 build order
"""
dependencies:
(a, d), (f, b), (b, d), (f, a), (d, c)
d.children.append(a)
b.children.append(f)
d.children.append(b)
a.children.append(f)
c.children.append(d)

  d         b       a       c
a   b     f       f       d

       c
      /
     d
    / \
   a   b
    \ /
     f
e/f, a/b, d, c

for all pairs:
build dependency graph or tree

iterate thru projects. if a project has no dependencies, add project to build order
if all a project's dependencies are already in the build order, add project to build order
continue until all projects are built 
"""
