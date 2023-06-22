import unittest

from ctci.ctci_2 import Node, generate_fruits_ll
from ctci.ctci_3 import MinStack, SetOfStacks, StackLL


class Ctci3(unittest.TestCase):
    def test_3_2(self):
        min_stack = MinStack(5)
        # (5) -> None
        self.assertEqual(1, min_stack.get_length())
        self.assertEqual(5, min_stack.get_min())
        min_stack.push(6)
        # (6) -> (5) -> None
        self.assertEqual(2, min_stack.get_length())
        self.assertEqual(5, min_stack.get_min())
        min_stack.push(3)
        # (3) -> (6) -> (5) -> None
        self.assertEqual(3, min_stack.get_length())
        self.assertEqual(3, min_stack.get_min())
        min_stack.push(7)
        # (7) -> (3) -> (6) -> (5) -> None
        self.assertEqual(4, min_stack.get_length())
        self.assertEqual(3, min_stack.get_min())
        popped_1 = min_stack.pop()
        # (3) -> (6) -> (5) -> None
        self.assertEqual(7, popped_1.value)
        self.assertEqual(3, min_stack.get_min())
        popped_2 = min_stack.pop()
        # (6) -> (5) -> None
        self.assertEqual(3, popped_2.value)
        self.assertEqual(5, min_stack.get_min())
        min_stack.push(4)
        # (4) -> (6) -> (5) -> None
        min_stack.push(4)
        # (4) -> (4) -> (6) -> (5) -> None
        popped_3 = min_stack.pop()
        # (4) -> (6) -> (5) -> None
        self.assertEqual(4, popped_3.value)
        self.assertEqual(4, min_stack.get_min())

    def test_3_3(self):
        set_of_stacks = SetOfStacks("apple", 5)
        # (('apple'))
        set_of_stacks.stacks.push("berry")
        set_of_stacks.stacks.push("cherry")
        set_of_stacks.stacks.push("durian")
        set_of_stacks.stacks.push("elderberry")
        set_of_stacks.stacks.push("fig")
        set_of_stacks.stacks.push("grapefruit")
        print(set_of_stacks.stacks)
        # (
        #   ('grapefruit') ->
        #   ('fig')
        # ) ->
        # (
        #   ('elderberry') ->
        #   ('durian') ->
        #   ('cherry') ->
        #   ('berry') ->
        #   ('apple')
        # )

        # Expected since peek returns the value of the node, not the node itself
        self.assertIsInstance(set_of_stacks.stacks.peek(), str)
        self.assertIsInstance(set_of_stacks.stacks, StackLL)
        self.assertEqual(2, set_of_stacks.stacks.get_length())
