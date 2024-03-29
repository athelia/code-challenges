from ctci_2 import (
    Node,
    LinkedList,
    delete_middle_node,
    generate_fruits_ll,
    sum_lists_ones_digit_at_head,
    sum_lists_ones_digit_at_tail,
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

    def test_2_4(self):
        ll1 = LinkedList.listify_integer(3585921, True)
        ll1.partition(5)
        self.assertEqual(LinkedList.listify_integer(3215958, True), ll1)

        ll2 = LinkedList.listify_integer(1295853, True)
        ll2.partition(5)
        self.assertEqual(LinkedList.listify_integer(1235859, True), ll2)

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

        # 7 -> 1 -> 6 + 5 -> 0 -> 4 = 2 -> 2 -> 0 -> 1
        ll4 = LinkedList.listify_integer(405)
        result_3 = sum_lists_ones_digit_at_head(ll1, ll4)
        self.assertEqual(result_3, LinkedList.listify_integer(1022))
        self.assertEqual(2, result_3.head.value)
        self.assertEqual(2, result_3.head.next.value)
        self.assertEqual(0, result_3.head.next.next.value)
        self.assertEqual(1, result_3.tail.value)

    def test_2_5_b(self):
        # Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
        # Output: 9 -> 1 -> 2. That is, 912.
        ll1 = LinkedList.listify_integer(617, True)
        ll2 = LinkedList.listify_integer(295, True)
        result = sum_lists_ones_digit_at_tail(ll1, ll2)
        self.assertEqual(result, LinkedList.listify_integer(912, True))

        ll3 = LinkedList.listify_integer(3, True)
        result_2 = sum_lists_ones_digit_at_tail(ll1, ll3)
        self.assertEqual(result_2, LinkedList.listify_integer(620, True))

        ll4 = LinkedList.listify_integer(405, True)
        result_3 = sum_lists_ones_digit_at_tail(ll1, ll4)
        self.assertEqual(result_3, LinkedList.listify_integer(1022, True))

    def test_2_6(self):
        ll1 = generate_fruits_ll(3)  # apple, berry, cherry
        ll1.extend([Node(fruit) for fruit in ["berry", "apple"]])
        self.assertTrue(ll1.is_palindrome())
        ll1.append(Node("apple"))
        self.assertFalse(ll1.is_palindrome())

        ll2 = LinkedList(Node("apple"))
        self.assertTrue(ll2.is_palindrome())
        ll2.append(Node("apple"))
        self.assertTrue(ll2.is_palindrome())

    def test_2_7(self):
        beet = Node("beet")
        ll1 = LinkedList(Node("arugula"))
        ll1.append(beet)
        ll2 = LinkedList(Node("asparagus"))
        ll2.append(beet)
        self.assertEqual(beet, ll1.intersects_at(ll2))

        ll3 = generate_fruits_ll(3)
        self.assertIsNone(ll3.intersects_at(ll1))
