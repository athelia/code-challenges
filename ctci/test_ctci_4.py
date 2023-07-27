import unittest

from ctci.ctci_4 import BinaryTreeNode, BinaryTree, Heap


class Ctci4(unittest.TestCase):
    def test_make_binary_tree(self):
        a = BinaryTreeNode("a")
        self.assertEqual(a.data, "a")
        a.left = b = BinaryTreeNode("b")
        a.right = c = BinaryTreeNode("c")
        b.left = d = BinaryTreeNode("d")
        b.right = BinaryTreeNode("e")
        c.left = BinaryTreeNode("f")
        c.right = g = BinaryTreeNode("g")
        tree = BinaryTree(a)
        self.assertEqual(tree.dfs("d"), d)
        self.assertEqual(tree.bfs("g"), g)

    def test_heap(self):
        root = BinaryTreeNode(5)
        heap = Heap(root)
        self.assertEqual(heap.root, root)
