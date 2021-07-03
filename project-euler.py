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

print(sum_even_fib(32))

def is_prime(x):
    for i in range(x//2):
        pass

def largest_prime_factor(n):
    for i in range(n/2):
        if n % i == 0:
            factor = n / i
            if is_prime(factor):
                return factor