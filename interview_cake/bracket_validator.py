import unittest


def is_valid(code):
    # Determine if the input code is valid
    closers = {")": "(", "]": "[", "}": "{"}
    openers = "({["
    stack = []
    for char in code:
        # This would be nice to generalize in case of other identical opener/closers, e.g. '' and ""
        if char == "|":
            # Peek to see if there's a pipe to close, otherwise add a pipe to the stack
            if not stack or stack[-1] != "|":
                stack.append("|")
            else:
                stack.pop()
        elif char in openers:
            stack.append(char)
        elif char in closers:
            try:
                last_open = stack.pop()
            except IndexError:
                # No open brackets in the stack
                return False
            complement = closers[char]
            if complement != last_open:
                # Trying to close a different bracket than last opened
                return False
    # Have all opened brackets been closed?
    return stack == []


# Tests
class Test(unittest.TestCase):
    def test_valid_short_code(self):
        result = is_valid("()")
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid("([]{[]})[]{{}()}")
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid("([)]")
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid("([][]}")
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid("[[]()")
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid("[[]]())")
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid("")
        self.assertTrue(result)

    def test_valid_pipes(self):
        result = is_valid("([{||}])")
        self.assertTrue(result)

    def test_extra_pipes(self):
        result = is_valid("([{||}|]|)")
        self.assertFalse(result)

    def test_insufficient_pipes(self):
        result = is_valid("()[]{}||{}|[]()")
        self.assertFalse(result)


unittest.main(verbosity=2)
