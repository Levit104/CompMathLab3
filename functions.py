import math


class Function:
    def __call__(self, x: float) -> float:
        pass


class Function1(Function):
    def __call__(self, x):
        return 4 * x ** 3 - 5 * x ** 2 + 6 * x - 7

    def __str__(self):
        return '4x^3 - 5x^2 + 6x - 7'


class Function2(Function):
    def __call__(self, x):
        return 2 * x + math.cos(x) - 4

    def __str__(self):
        return '2x + cos(x) - 4'


class Function3(Function):
    def __call__(self, x):
        return 1 / (1 + abs(x)) + 3 * x

    def __str__(self):
        return '1 / (1 + |x|) + 3x'


functions: dict[int, Function] = {
    1: Function1(),
    2: Function2(),
    3: Function3()
}
