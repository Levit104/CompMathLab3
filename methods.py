def left_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def right_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + h + i * h) for i in range(n))


def middle_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + h / 2 + i * h) for i in range(n))


def trapezoid(f, a, b, n):
    h = (b - a) / n
    temp_sum = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + temp_sum)
    # return h / 2 * (f(a) + f(b) + 2 * temp_sum)


def simpson(f, a, b, n):
    h = (b - a) / n
    temp_sum1 = sum(f(a + i * h) for i in range(1, n, 2))
    temp_sum2 = sum(f(a + i * h) for i in range(2, n, 2))
    return (h / 3) * (f(a) + 4 * temp_sum1 + 2 * temp_sum2 + f(b))


methods = {
    1: (left_rectangles, 'Метод левых прямоугольников'),
    2: (right_rectangles, 'Метод правых прямоугольников'),
    3: (middle_rectangles, 'Метод средних прямоугольников'),
    4: (trapezoid, 'Метод трапеций'),
    5: (simpson, 'Метод Симпсона'),
}
