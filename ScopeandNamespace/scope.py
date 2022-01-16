def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result


def factorial(n):
    """Calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        n * factorial(n - 1)


def fib(n):
    """f(n) = f(n -1) + f(n -2)"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(36):
    print(i, fact(i))
