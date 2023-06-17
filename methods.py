from functions import Function


class Method:
    k: int

    def solve(self, f: Function, a: float, b: float, n: int, h: float) -> float:
        pass

    def __call__(self, f: Function, a: float, b: float, n: int, eps: float,
                 print_info: bool = True) -> tuple[float, int]:
        h: float = (b - a) / n
        i0: float = self.solve(f, a, b, n, h)

        while True:
            n *= 2
            h = (b - a) / n

            i1: float = self.solve(f, a, b, n, h)
            runge_check: float = abs(i1 - i0) / (2 ** self.k - 1)

            if print_info:
                print(f'\nN = {int(n / 2)} * 2 = {n}'
                      f'\n|I1 - I0| / (2^k - 1) = |({i1}) - ({i0})| / {2 ** self.k - 1} = {runge_check}')

            if runge_check <= eps:
                break

            i0 = i1

        if i0 == i1:
            n = int(n / 2)

        return i1, n


class LeftRectangles(Method):
    k = 1

    def solve(self, f, a, b, n, h):
        return h * sum(f(a + i * h) for i in range(n))

    def __str__(self):
        return 'Метод левых прямоугольников'


class RightRectangles(Method):
    k = 1

    def solve(self, f, a, b, n, h):
        return h * sum(f(a + h + i * h) for i in range(n))

    def __str__(self):
        return 'Метод правых прямоугольников'


class MiddleRectangles(Method):
    k = 2

    def solve(self, f, a, b, n, h):
        return h * sum(f(a + h / 2 + i * h) for i in range(n))

    def __str__(self):
        return 'Метод средних прямоугольников'


class Trapezoid(Method):
    k = 2

    def solve(self, f, a, b, n, h):
        temp_sum = sum(f(a + i * h) for i in range(1, n))
        return h * ((f(a) + f(b)) / 2 + temp_sum)

    def __str__(self):
        return 'Метод трапеций'


class Simpson(Method):
    k = 4

    def solve(self, f, a, b, n, h):
        temp_sum1 = sum(f(a + i * h) for i in range(1, n, 2))
        temp_sum2 = sum(f(a + i * h) for i in range(2, n, 2))
        return (h / 3) * (f(a) + 4 * temp_sum1 + 2 * temp_sum2 + f(b))

    def __str__(self):
        return 'Метод Симпсона'


methods: dict[int, Method] = {
    1: LeftRectangles(),
    2: RightRectangles(),
    3: MiddleRectangles(),
    4: Trapezoid(),
    5: Simpson()
}
