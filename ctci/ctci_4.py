# CTCI Chapter 4, Trees and Graphs
from typing import Any, Optional


class BinaryTreeNode:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<BinaryTreeNode data={self.data} left={self.left} right={self.right}>"


class TreeNode:
    def __init__(self, data: Any):
        self.data = data
        self.children = []

    def __repr__(self):
        return f"<TreeNode data={self.data} children={self.children}>"


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def dfs(self, target: Any) -> Optional[BinaryTreeNode]:
        to_search = [self.root]
        while to_search:
            current = to_search.pop()
            if target == current.value:
                return current
            to_search.extend([current.left, current.right])
