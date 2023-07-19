import unittest

from ctci.ctci_4 import BinaryTreeNode


class Ctci3(unittest.TestCase):
    def test_make_binary_tree(self):
        a = BinaryTreeNode("a")
        self.assertEqual(a.data, "a")
