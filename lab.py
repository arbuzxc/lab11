# Николенко 107б
import math


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (x1, x2)


def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)
