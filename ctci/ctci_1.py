# CTCI Chapter 1, Arrays and Strings

# 1.1: Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def is_unique_simple(string: str) -> bool:
    """ Easy to read and write Pythonic implementation. O(n) runtime, O(n) space

        Args:
            string (str): String to be evaluated for unique characters
        Returns:
            bool: whether all characters are unique
    """
    return len(set(string)) == len(string)


def is_unique_sorted_string(string: str) -> bool:
    """ Use a sorted string for a compromise between space and runtime. O(n * log n) runtime, O(n) space"""
    if len(string) < 2:
        return True
    for i, char in enumerate(sorted(string[1:])):
        if string[i+1] == char:
            return False
    return True


def is_unique_no_additional_data_structures(string: str) -> bool:
    """ Use a nested loop for best space. O(n^2) runtime, O(1) space"""
    for i in range(len(string) - 1):
        for j in range(i, len(string)):
            if string[i] == string[j]:
                return False
    return True


# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "tacocat" , "atcocta" , etc.)

def is_anagram_of_palindrome_hashmap(string: str) -> bool:
    counts = {}
    for char in string:
        counts[char] += counts.get(char, 0)
    odd_count_seen = False
    for count in counts:
        if count % 2 == 1:
            if odd_count_seen:
                return False
            else:
                odd_count_seen = True
    return True


def is_anagram_of_palindrome(string: str) -> bool:
    pass
