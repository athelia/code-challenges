from ctci_2 import (
    Node,
    LinkedList,
    delete_middle_node,
    generate_fruits_ll,
    sum_lists_ones_digit_at_head,
    listify_integer,
)
import unittest


class Ctci2(unittest.TestCase):
    def test_setup(self, verbose: bool = False):
        if verbose:
            print("Setup")
        n1 = Node("apple")
        n2 = Node("berry")
        n3 = Node("cherry")
        n4 = Node("durian")
        n5 = Node("apple")
        ll = LinkedList(n1)
        self.assertIsInstance(ll, LinkedList)
        ll.append(n2)
        ll.append(n3)
        lgth = ll.get_length()
        self.assertTrue(lgth == 3)
        if verbose:
            print(f"length={lgth}")
            ll.traverse_and_print()
        self.assertIsInstance(ll.find("berry"), Node)
        ll.delete("berry", verbose=verbose)
        if verbose:
            ll.traverse_and_print()
        self.assertIs(None, ll.find("berry"))
        n2.next = (
            None  # otherwise n2.next is still pointing to n3, leading to a circular ll
        )
        ll.extend([n2, n4, n5])
        ll.extend([Node(fruit) for fruit in ["elderberry", "fig", "grapefruit"]])
        if verbose:
            print(f"ll={ll}")

    def test_2_1(self, verbose: bool = False):
        ll = generate_fruits_ll(8, verbose=verbose)
        ll.extend(
            [Node(fruit) for fruit in ["apple", "apple", "honeydew", "grapefruit"]],
            verbose=verbose,
        )
        if verbose:
            print("2.1 Remove duplicates")
            ll.traverse_and_print()
        ll.remove_dupes()
        if verbose:
            ll.traverse_and_print()
        self.assertEqual(10, ll.get_length())
        # TODO: is there a better/another assertion?

    def test_2_2(self, verbose: bool = False):
        ll = generate_fruits_ll(15, verbose=verbose)
        if verbose:
            print("2.2Return kth to last")
            ll.traverse_and_print()
            print(f"7th to last={ll.return_kth_to_last(7).value}")
            print(f"12th to last={ll.return_kth_to_last(12).value}")
        self.assertEqual("ice apple", ll.return_kth_to_last(7).value)
        self.assertEqual("durian", ll.return_kth_to_last(12).value)

    def test_2_3(self, verbose: bool = False):
        ll = generate_fruits_ll(10)
        durian = ll.find("durian")
        ice_apple = ll.find("ice apple")

        if verbose:
            print("2.3 Delete middle node")
            ll.traverse_and_print()
            print(f"Deleting durian node...")

        delete_middle_node(durian, verbose=verbose)
        cherry = ll.find("cherry")
        self.assertEqual("elderberry", cherry.next.value)

        if verbose:
            ll.traverse_and_print()
            print(f"Deleting ice apple node...")

        delete_middle_node(ice_apple, verbose=verbose)
        honeydew = ll.find("honeydew")
        self.assertEqual("jackfruit", honeydew.next.value)

        if verbose:
            ll.traverse_and_print()

    def test_2_5(self, verbose: bool = False):
        # Input: ( 7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
        # Output: 2 -> 1 -> 9. That is, 912.
        if verbose:
            print("2.5 Sum lists")
            print("v1: head = ones digit, same length")
        ll1 = LinkedList.listify_integer(617)
        ll2 = LinkedList.listify_integer(295)
        result = sum_lists_ones_digit_at_head(ll1, ll2)
        self.assertEqual(result, LinkedList.listify_integer(912))
        self.assertEqual(2, result.head.value)
        self.assertEqual(1, result.head.next.value)
        self.assertEqual(9, result.tail.value)

        # 7 -> 1 -> 6 + 3 = 0 -> 2 -> 6
        ll3 = LinkedList.listify_integer(3)
        result_2 = sum_lists_ones_digit_at_head(ll1, ll3)
        self.assertEqual(result_2, LinkedList.listify_integer(620))
        self.assertEqual(0, result_2.head.value)
        self.assertEqual(2, result_2.head.next.value)
        self.assertEqual(6, result_2.tail.value)
