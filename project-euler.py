def sum_multiples(ceiling, multiple):
    """Given a ceiling (inclusive), calculate the sum of all numbers that are multiples of the multiple."""
    terms = ceiling // multiple
    return multiple * (terms * (terms + 1)) / 2

# sum_fifteen = sum_multiples(999, 3) + sum_multiples(999, 5) - sum_multiples(999, 15)
# print(sum_fifteen)

def fibonacci(n, memo={}):
    if memo.get(n):
        return memo[n]
    
    if n <= 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# print(fibonacci(32)) #3524578
def sum_even_fib(ceiling):
    total = 0
    for i in range(ceiling + 1): #TODO: improved efficiency summing only every 3rd fib
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
    #Primes are of the form 6n +/- 1. Test 5 and 5+2 (7), 5+6 (11) and 5+6+2 (13), etc.
    while factor <= x // 2 + 1:
        # print('/t',factor)
        if x % factor == 0 or x % (factor + 2) == 0:
            return False
        factor += 6
    return True

# print(is_prime(5003))

def largest_prime_factor(n):
    for i in range(2, n//2 + 1):
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
    for i in range(n, n//10, -1):
        for j in range(n, n//10, -1):
            if is_palindrome(str(i * j)):
                products.append(i * j)
    return max(products)

# print(find_palindrome_products(999))

# Euler 5 - divisible by 1 - 20
# Primes: 2, 3, 5, 7, 11, 13, 17, 19

def is_square(n):
    return int(n**0.5) == (n ** 0.5)

def is_cube(n):
    return int(n ** (1/3)) == (n ** (1/3))

def is_4th_power(n):
    return int(n ** (1/4)) == (n ** (1/4))

def factors_up_to(n):
    """Return a list of all factors up to + inclusive of n"""
    factors = []
    for i in range(1, n + 1):
        if is_prime(i) or is_square(i) or is_cube(i) or is_4th_power(i):
            factors.append(i)
    return factors

def smallest_multiple(n):
    """Calculate the smallest number divisble by all numbers up to n"""
    factors = factors_up_to(n)
    multiple = 1
    print(factors)
    for factor in factors:
        if multiple % factor != 0:
            print('multiple', multiple, 'factor', factor)
            if is_square(factor):
                multiple *= (factor ** 0.5)
            elif is_cube(factor):
                multiple *= (factor ** (1/3))
            elif is_4th_power(factor):
                multiple *= (factor ** (1/4))
            else:
                multiple *= factor
    return multiple

# print(smallest_multiple(20))
# actual solution is 232792560
# function returns   465585120
# extra *2 somewhere.... :( probably with the 4th power thingy