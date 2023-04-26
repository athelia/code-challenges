import unittest


def merge_ranges(meetings):
    # Merge meeting ranges
    return merge_ranges_better(meetings)


def merge_ranges_naive(meetings):
    # O(n ^ 2)

    # simplest: check each new range against a list of tuples to see if start time falls inside
    # merged range is the result of

    results = [] if not meetings else [meetings[0]]

    for meeting in meetings:
        overlap_found = False
        for i, result in enumerate(results):
            # start time or end time of meeting falls between an existing result range
            if result[0] <= meeting[0] <= result[1] or result[0] <= meeting[1] <= result[1]:
                overlap_found = True
                # use the least start time and most end time and replace the range
                results[i] = (min(result[0], meeting[0]), max(result[1], meeting[1]))
        # otherwise we'll need to make a new range
        if not overlap_found:
            results.append((meeting[0], meeting[1]))

    return sorted(results)


# WIP
def merge_ranges_better(meetings):
    """ Sort first, then merge as long as new meeting falls within current range.
        O(n * log(n))

        >>> [(0, 2), (1, 5)]
        [(0, 5)]
        >>> [(1, 2), (3, 4)]
        [(1, 2), (3, 4)]
    """

    results = []
    sorted_meetings = sorted(meetings)
    i = 0

    while i < len(sorted_meetings) - 1:
        result = sorted_meetings[i]
        j = i + 1
        # as long as the start time of j is between start and end time of i
        while sorted_meetings[i][0] <= sorted_meetings[j][0] <= sorted_meetings[i][1] and j < len(sorted_meetings) - 1:
            # sorted already, so start times will be earlier for i
            result = (sorted_meetings[i][0], max(sorted_meetings[i][1], sorted_meetings[j][1]))
            j += 1
        # we've already consumed everything within the range, so skip ahead
        results.append(result)
        i = j
    return results


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)