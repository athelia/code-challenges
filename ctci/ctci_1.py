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
    """ Use a sorted string as an alternative. O(n * log n) runtime, O(n) space"""
    if len(string) < 2:
        return True
    sorted_string = sorted(string)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i+1] == sorted_string[i]:
            return False
    return True


def is_unique_no_additional_data_structures(string: str) -> bool:
    """ Use a nested loop for best space. O(n^2) runtime, O(1) space"""
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
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
        if char in ([" ", ".", ",", "!", "-", "_", ":", ";", "?"]):
            continue
        else:
            counts[char.lower()] = counts.get(char.lower(), 0) + 1
    odd_count_seen = False
    for letter in counts:
        if counts[letter] % 2 == 1:
            if odd_count_seen:
                return False
            else:
                odd_count_seen = True
    return True


# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress_string(string: str) -> str:
    result = ""
    current_count = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            result += string[i] + str(current_count)
        elif string[i + 1] == string[i]:
            current_count += 1
        else:
            result += string[i] + str(current_count)
            current_count = 1
    return string if len(string) < len(result) else result


if __name__ == "__main__":
    print("\n\nCTCI 1.1")
    print(f"Testing is_unique_simple('')={is_unique_simple('')}")
    print(f"Testing is_unique_simple('abcd')={is_unique_simple('abcd')}")
    print(f"Testing is_unique_simple('aba')={is_unique_simple('aba')}")
    print(f"Testing is_unique_no_additional_data_structures('')={is_unique_no_additional_data_structures('')}")
    print(f"Testing is_unique_no_additional_data_structures('abcd')={is_unique_no_additional_data_structures('abcd')}")
    print(f"Testing is_unique_no_additional_data_structures('aba')={is_unique_no_additional_data_structures('aba')}")
    print(f"Testing is_unique_sorted_string('')={is_unique_sorted_string('')}")
    print(f"Testing is_unique_sorted_string('abcd')={is_unique_sorted_string('abcd')}")
    print(f"Testing is_unique_sorted_string('aba')={is_unique_sorted_string('aba')}")
    print("\n\nCTCI 1.4")
    print(f"Testing is_anagram_of_palindrome_hashmap('')={is_anagram_of_palindrome_hashmap('')}")
    print(f"Testing is_anagram_of_palindrome_hashmap('tactcoa')={is_anagram_of_palindrome_hashmap('tactcoa')}")
    print(f"Testing is_anagram_of_palindrome_hashmap('Tact Coa')={is_anagram_of_palindrome_hashmap('Tact Coa')}")
    print("\n\nCTCI 1.6")
    print(f"Testing compress_string('')={compress_string('')}")
    print(f"Testing compress_string('aabcccccaaa')={compress_string('aabcccccaaa')}")
    print(f"Testing compress_string('abcde')={compress_string('abcde')}")

