def sum_multiples(ceiling, multiple):
    """Given a ceiling (inclusive), calculate the sum of all numbers that are multiples of the multiple."""
    terms = ceiling // multiple
    return multiple * (terms * (terms + 1)) / 2

sum_fifteen = sum_multiples(999, 3) + sum_multiples(999, 5) - sum_multiples(999, 15)
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
    for i in range(ceiling + 1):
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

print(largest_prime_factor(600851475143))