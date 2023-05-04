def sum_multiples(ceiling, multiple):
    """Given a ceiling (inclusive), calculate the sum of all numbers that are multiples of the multiple."""
    terms = ceiling // multiple
    return multiple * (terms * (terms + 1)) / 2


# sum_fifteen = sum_multiples(999, 3) + sum_multiples(999, 5) - sum_multiples(999, 15)
# print(sum_fifteen)


def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if memo.get(n):
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# print(fibonacci(32)) #3524578
def sum_even_fib(ceiling):
    total = 0
    for i in range(ceiling + 1):  # TODO: improved efficiency summing only every 3rd fib
        if fibonacci(i) % 2 == 0:
            total += fibonacci(i)
    return total


# print(sum_even_fib(32))


def is_prime(x):
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
        return True
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    factor = 5
    # Primes are of the form 6n +/- 1. Test 5 and 5+2 (7), 5+6 (11) and 5+6+2 (13), etc.
    while factor <= x // 2 + 1:
        # print('/t',factor)
        if x % factor == 0 or x % (factor + 2) == 0:
            return False
        factor += 6
    return True


# print(is_prime(5003))


def largest_prime_factor(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factor = n / i
            if is_prime(factor):
                return factor


# print(largest_prime_factor(600851475143))


def is_palindrome(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


# print(is_palindrome('racecar'))
# print(is_palindrome(str(1001)))


def find_palindrome_products(n):
    """Largest palindrome product of two digits up to value n"""
    products = []
    for i in range(n, n // 10, -1):
        for j in range(n, n // 10, -1):
            if is_palindrome(str(i * j)):
                products.append(i * j)
    return max(products)


# print(find_palindrome_products(999))

# Euler 5 - divisible by 1 - 20
# Primes: 2, 3, 5, 7, 11, 13, 17, 19


def is_square(n):
    return int(n ** 0.5) == (n ** 0.5)


def is_cube(n):
    return int(n ** (1 / 3)) == (n ** (1 / 3))


def is_4th_power(n):
    return int(n ** (1 / 4)) == (n ** (1 / 4))


def factors_up_to(n):
    """Return a list of all factors up to + inclusive of n"""
    factors = []
    for i in range(1, n + 1):
        if is_prime(i) or is_square(i) or is_cube(i) or is_4th_power(i):
            factors.append(i)
    return factors


def smallest_multiple(n):
    """Calculate the smallest number divisible by all numbers up to n"""
    factors = factors_up_to(n)
    multiple = 1
    print(factors)
    for factor in factors:
        if multiple % factor != 0:
            print("multiple", multiple, "factor", factor)
            if is_square(factor):
                multiple *= factor ** 0.5
            elif is_cube(factor):
                multiple *= factor ** (1 / 3)
            elif is_4th_power(factor):
                multiple *= factor ** (1 / 4)
            else:
                multiple *= factor
    return multiple


# print(smallest_multiple(20))
# actual solution is 232792560
# function returns   465585120
# extra *2 somewhere.... :( probably with the 4th power thingy
# Perhaps a modulo approach instead?


def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total


def square_of_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total ** 2


# a = sum_of_squares(100)
# b = square_of_sum(100)
# c = b - a
# print(a, b, c)


def nth_prime(n):
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
    primes = [2, 3]
    i = 1
    if n <= 2:
        return primes[n - 1]
    else:
        while len(primes) < n:
            # generate next potential prime
            # check if prime
            # if yes then append
            # -> this is a little wasteful. could be more space efficient
            # if we keep a counter and only hang on to the most recent prime.
            possible_low = 6 * i - 1
            possible_high = 6 * i + 1
            if is_prime(possible_low):
                primes.append(possible_low)
            if is_prime(possible_high):
                primes.append(possible_high)
            i += 1
    # print(primes)
    return primes[n - 1]


# print(nth_prime(10001))


# Project Euler #8 https://projecteuler.net/problem=8
def largest_product_in_series(s):
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the 13 adjacent digits in the number that have the greatest product. What is the value of this product?
    """
    # Fixed window approach?
    # Keep 14 digits at a time so we can divide by first digit to get new product
    # TODO: While I think that the above approach is generally correct, I suspect I need two pointers
    #   to solve this successfully. Tabled in favor of grinding leetcodes for now.
    product = highest_product = multiply_all_elements(s[:14])
    i = 13
    while i < len(s) - 14:
        i = find_next_consecutive_without_zeroes(s, 13)
        product = product / s[i - 13] * s[i]
        highest_product = max(product, highest_product)
        i += 1
    return highest_product
    # Optimization: exempt any range including the digit 0


def multiply_all_elements(lst):
    """Helper function for largest product in series"""
    product = 1
    for digit in lst:
        product *= digit
    return product


def find_next_consecutive_without_zeroes(lst, substring_length):
    """Helper function to find long run of digits without zeroes"""
    i = 0
    max_substring_found = 0
    while max_substring_found <= substring_length and i < len(lst):
        if lst[i] == 0:
            max_substring_found = 0
        else:
            max_substring_found += 1
            if max_substring_found == substring_length:
                break
        i += 1
    if max_substring_found == substring_length:
        # return the starting position of the substring
        return i - (substring_length - 1)
    else:
        return None


large_number = "\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

# print(largest_product_in_series([int(digit) for digit in large_number]))
print(find_next_consecutive_without_zeroes([int(digit) for digit in large_number], 13))
print(
    find_next_consecutive_without_zeroes(
        [int(digit) for digit in large_number][45:], 13
    )
)
