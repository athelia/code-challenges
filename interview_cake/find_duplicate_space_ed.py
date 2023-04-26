# InterviewCake: https://www.interviewcake.com/question/python3/find-duplicate-optimize-for-space

import unittest


def find_repeat(numbers):
    # Find a number that appears more than once

    floor, ceiling = 1, len(numbers)

    while floor < ceiling:
        midpoint = floor + (ceiling - floor) // 2
        low_bound_floor, low_bound_ceiling = floor, midpoint
        high_bound_floor, high_bound_ceiling = midpoint + 1, ceiling
        count_low, count_high = 0, 0

        for n in numbers:
            if low_bound_floor <= n <= low_bound_ceiling:
                count_low += 1

        # e.g. range(4, 8) has 5 unique integers: 4, 5, 6, 7, 8
        low_bound_unique_integers = low_bound_ceiling - low_bound_floor + 1

        if count_low > low_bound_unique_integers:
            floor, ceiling = low_bound_floor, low_bound_ceiling
        else:
            floor, ceiling = high_bound_floor, high_bound_ceiling

    return floor


'''
Things not to forget:
  - add floor to midpoint calculation: floor + (ceiling - floor) // 2
  - start the high bound at midpoint + 1
  - only need to store & compare 1 set of possibilities (low bound or high bound) - but need to keep track of both possible ranges
'''


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
