def sum_multiples(ceiling, multiple):
    """Given a ceiling (inclusive), calculate the sum of all numbers that are multiples of the multiple."""
    terms = ceiling // multiple
    return multiple * (terms * (terms + 1)) / 2

sum_fifteen = sum_multiples(999, 3) + sum_multiples(999, 5) - sum_multiples(999, 15)
print(sum_fifteen)

