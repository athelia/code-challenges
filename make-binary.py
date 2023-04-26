def make_binary(n):
    """Given a positive integer, return its binary representation as a list
    >>> 4
    [1, 0, 0]
    >>> 1
    [1]
    >>> 15
    [1, 1, 1, 1]
    """
    result = []
    while n > 0:
        result.append(n % 2)
        n = n // 2
    result.reverse()
    return result


print(make_binary(4) == [1, 0, 0])
print(make_binary(1) == [1])
print(make_binary(15) == [1, 1, 1, 1])
