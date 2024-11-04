from ast import Raise


def sum(a, b):
    return a + b


def substract(a, b):
    return a - b


def divisor(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def product(a, b):
    return a*b
