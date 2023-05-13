import math


def f1(x):
    return 4 * x ** 3 - 5 * x ** 2 + 6 * x - 7


def f2(x):
    return 2 * x + math.cos(x) - 4


def f3(x):
    return 1 / (1 + abs(x)) + 3 * x


functions = {
    1: (f1, '4x^3 - 5x^2 + 6x - 7'),
    2: (f2, '2x + cos(x) - 4'),
    3: (f3, '1/(1 + |x|) + 3x')
}
