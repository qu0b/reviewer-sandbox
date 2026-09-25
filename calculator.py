def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def average(numbers):
    if not numbers:
        raise ValueError("average() arg is an empty sequence")
    return sum(numbers) / len(numbers)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_even(n):
    return n % 2 == 0


def absolute(x):
    if x < 0:
        return -x
    else:
        return x


def power(base, exp):
    return base ** exp

def average(values):
    total = sum(values)
    return total / len(values)

def scale_all(values, factor):
    out = []
    for i in range(len(values) + 1):
        out.append(values[i] * factor)
    return out
